from queue import PriorityQueue
import heapq
# quai_identifier
attri = {'age':0,'education_num':4}
attri_name = list(attri)
# domain of quai_indentifier
init_range_list = [(0,99),(0,19)]
# k stands for k_anonymity
k = 90 
data = open("./K-Anonymity实验数据/adult.data","r")
records = data.readlines()


# range_tree
# internal node represent attribute domain
# like age:[0-19] education_num:[5-10]
# leaf node represent a set of record who's attribute with it's parent's range
# Function:
# add_child() add_leaf() used to add leaf and internal node
# split() used to split domain_range half_by_half
class range_tree:
    # init a tree node with domain given
    # domain should be a list of tuples ,examples
    # [(lowerbound,upperbound),(lowerbound,upperbound)]
    # domain name like follow
    # [age,education_num]
    # child is sub_range_tree 
    # leaf is node of record
    # leaf_count is # of record in range rather than leaf_dict key count
    def __init__(self,domain_name,domain_list):
        self.child_list = []
        self.leaf_dict = {} 
        self.leaf_count = 0
        self.parent = None
        self.depth = 0
        self.child_count = 0
        self.domain_name = domain_name
        self.domain_list = domain_list

    # new_tree_node should be a range_tree node
    def add_child(self,new_tree_node):
        self.child_list.append(new_tree_node)
        self.child_count += 1
        new_tree_node.parent = self
        new_tree_node.depth = self.depth + 1
    
    # record will be seperated into attribute items
    # leaf node of range_tree will be stored in form of dict like below:
    # {(attri1,attri2..):[list of records]}
    def add_leaf(self,record):
        attri_items = record.split(",")
        dict_key = []
        # get attribute(domain) value of record
        for domain in self.domain_name:
            new_attri = int(attri_items[attri[domain]].strip())
            dict_key.append(new_attri)
        # use tuple to make it hashable(so can be used in dict)
        new_key = tuple(dict_key)
        if new_key in self.leaf_dict:
            self.leaf_dict[new_key].append(record)
        else:
            self.leaf_dict[new_key] = [record]
        self.leaf_count += 1 
        
    # used to add multiple records as leaf to a range_tree node
    # key is a tuple as (attri1,attri2 ...)
    # records is a list of record accord to key
    def add_leaves(self,key,records):
        self.leaf_count += len(records)
        if key in self.leaf_dict:
            self.leaf_dict[key].extend(records)
        else:
            self.leaf_dict[key] = records

    # used to debug
    # see self as root ,print the whold tree
    # each child and leaf as a new line
    def print_tree(self):
        i = 0
        while i < self.depth:
            print("  ",end = "")
            i += 1
        print("-\\",end = "")
        for domain_range in self.domain_list:
            print("[",domain_range[0],",",domain_range[1],"]",end = "")
        print("leaf_count:",self.leaf_count)
        for key in self.leaf_dict.keys():
            i = 0
            while i < self.depth + 1:
                print("  ",end = "")
                i += 1
            print("-|",end = "")
            print(key)
        for child in self.child_list:
            child.print_tree()

    # split the tree according to attribute of domain_name
    # the domain will be split into half half
    # the leaves will get migrated too
    # if the split will violate k_annyomity,split will terminate 
    # return True if split sucessfully else False
    def split_tree(self,domain_name,k):
        if self.child_count != 0:
            print("cannot split node with child")
            exit(0)
        left_domain_list = []
        right_domain_list = []
        left_domain_list.extend(self.domain_list)
        right_domain_list.extend(self.domain_list)
        name_index = self.domain_name.index(domain_name)
        lowerbound = self.domain_list[name_index][0]
        upperbound = self.domain_list[name_index][1]
        mid = (upperbound + lowerbound) // 2
        left_domain_list[name_index] = (lowerbound,mid)
        leftchild = range_tree(self.domain_name,left_domain_list)
        right_domain_list[name_index] = (mid,upperbound)
        rightchild = range_tree(self.domain_name,right_domain_list)
        #put leaf node to splited internal node
        for key in self.leaf_dict.keys():
            if key[name_index] <= mid:
                leftchild.add_leaves(key,self.leaf_dict[key])
            else:
                rightchild.add_leaves(key,self.leaf_dict[key])
        # if split will not violate k_anonymity
        # add splited node to parent
        if leftchild.leaf_count >= k and rightchild.leaf_count >= k:
            self.leaf_dict = {}
            self.add_child(leftchild)
            self.add_child(rightchild)
            return True
        else:
            return False

    # used by priority queue
    def __lt__(self,other):
        return self.leaf_count < other.leaf_count

    #check if parent node's leaf_count equal to sum of child's leaf_count
    def check_valid(self):
        child_leaf_count = 0
        if self.child_count == 0:
            return True
        for child in self.child_list:
            child_leaf_count += child.leaf_count
        if child_leaf_count != self.leaf_count:
            return False
        else:
            for child in self.child_list:
                if child.check_valid() == False:
                    return False
            return True

# read leaf node of range_tree node
# convert old_record to generalized record
# return in a list
def record_gene(range_tree):
    new_record_list = []
    for leaf in range_tree.leaf_dict:
        record_list = range_tree.leaf_dict[leaf]
        for record in record_list:
            items = record.split(",")
            for domain_name in range_tree.domain_name:
                name_index = range_tree.domain_name.index(domain_name)
                items[attri[domain_name]] = str(range_tree.domain_list[name_index][0]) + "~" + str(range_tree.domain_list[name_index][1])
            new_record = items.pop(0)
            for item in items:
                new_record += ' ,'
                new_record += item
            new_record_list.append(new_record)
    return new_record_list

# return generalized version of records in range_tree
# stored in global_new_records as a list
def generalize(range_tree,global_new_records):
    if range_tree.child_count == 0:
        new_records_list = record_gene(range_tree)
        global_new_records += new_records_list
    else:
        for child in range_tree.child_list:
            generalize(child,global_new_records)

        


# init range_tree
tree = range_tree(attri_name,init_range_list)
for record in records:
    tree.add_leaf(record)
records_count = len(records)

# use priority queue to decide next range_node to split
# priority is each node's leaf_count
# split the node with highest leaf_count first
node_queue = [] 
# initial node is first to be splited
heapq.heappush(node_queue,(records_count-tree.leaf_count,tree))

while len(node_queue) != 0:
    # get the node to split
    node_to_split = heapq.heappop(node_queue)[1]
    # get the domain_name of longest range in the node
    domain_name = node_to_split.domain_name[0]
    domain = node_to_split.domain_list[0]
    max_domain_lenght = domain[1] - domain[0]
    for domain in node_to_split.domain_list:
        new_domain_lenght = domain[1] - domain[0]
        if new_domain_lenght > max_domain_lenght:
            domain_name = node_to_split.domain_name[node_to_split.domain_list.index(domain)]
            max_domain_lenght = new_domain_lenght
    #split the node and enqueue new node
    #if longest domain cannot be splitted ,try other domain until success
    if node_to_split.split_tree(domain_name,k) == False:
        for remain_domain in node_to_split.domain_name:
            if remain_domain != domain_name:
                if node_to_split.split_tree(remain_domain,k):
                    break
    for child in node_to_split.child_list:
        heapq.heappush(node_queue,(records_count-child.leaf_count,child))

# generalize all the records in range_tree and write result in new file
tree.print_tree()
global_new_records = []
generalize(tree,global_new_records)
new_file = open("./K-Anonymity实验数据/new_mondrain_adult.data","w")
for new_record in global_new_records:
    new_file.write(new_record)
new_file.close()
