# Utility:
# represent generalization hierarchy
class tree:
    # data should be a string ,represent hierarchical item
    # like data = "alone" or data = "Male"
    def __init__(self,data,children = None): 
        self.data = data
        self.children = []
        if(children != None):
            for child in children:
                self.add_children(child)

    # child should be a tree node
    def add_children(self,child):
        self.children.append(child)

    # regard self as root of the tree
    # search for descendant node with given data
    # return the fisrt met offspring if exist
    # else return None
    def search(self,data): 
        if self.data == data: 
            return self 
        for node in self.children:
            result = node.search(data)
            if result != None:
                return result
        return None

    # Dubug
    # print each node in a line
    def print_tree(self,depth):
        i = 0
        while i < depth:
            print("  ",end = '')
            i = i+ 1
        if len(self.children) == 0:
            print("|-",self.data)
        else:
            print("\-",self.data)
            for child in self.children:
                child.print_tree(depth+1)

    # self should be predefined root of the tree
    # read record from file_path
    # split record into attributes and select certain attributes as data to build child   
    # node
    def read_and_construct(self,file_path):
        filename = open(file_path,"r")
        records = filename.readlines()
        for record in records:
            root_data = record.split(",")[1].strip()
            root = self.search(root_data)
            root.add_children(tree(record.split(",")[0]))
        filename.close()

    # used in samarati function
    # self should be root of the hierarchy tree
    # with layer "*"(all generalize) have depth 0
    # return all node with given depth in a list
    def get_children(self,depth):
        if depth == 0:
            return [self]
        else:
            child_list = [];
            for child in self.children:
                child_list = child_list + child.get_children(depth - 1)
            return child_list

    # search the tree from self
    # return data of child node haing "attribute"
    def check_and_change(self,attribute):
        if self.search(attribute) != None:
            return self.data
        else:
            return None

# generate vector of generalize depth
# (high,low): low < sumation(generalize vector) < high
# return list of generalize depth
def valid_vec_gen(high,low):
    mid = (high + low ) // 2
    valid_vecs = []
    for race_level in range(2):
        for gender_level in range(2):
            for marital_level in range(3):
                age_level = mid - race_level - gender_level - marital_level
                if age_level in range(5):
                    valid_vecs.append((marital_level,race_level,gender_level,age_level))
    return valid_vecs

# max_sup: max suppression number
# k : k-anonymity
# general_level_vec: generalize vector from previous function
# records : all records
# marital_status_tree : hierarchy tree of attribute marital_status
# race_tree : hierarchy tree of attribute race
# gender_tree : hierarchy tree of attribute gender
# age_tree : hierarchy tree of attribute age
# generalize : when set to true,function will return generalized records list
def satisfy(max_sup,k,general_level_vec,records,marital_status_tree,race_tree,gender_tree,age_tree,generalize = False):
    # get all node at given depth for each attribute
    marital_child_list = marital_status_tree.get_children(general_level_vec[0])
    race_child_list = race_tree.get_children(general_level_vec[1])
    gender_child_list = gender_tree.get_children(general_level_vec[2])
    age_child_list = age_tree.get_children(general_level_vec[3])
    # note how many times record appears with certain quai_identifier
    quai_to_number = {}
    quai_to_record = {}
    # used to generate new records
    new_records_list = []
    # sup_number : how many record should be supressed(sum of quai_cluster with less than 
    # k records)
    sup_number = 0
    # deal one record a time
    for record in records:
        # extract attribute value
        marital_info = record.split(",")[5].strip()
        race_info = record.split(",")[8].strip()
        gender_info = record.split(",")[9].strip()
        age_info = record.split(",")[0].strip()
        
        # check if record[certain attribute] is descendant of a tree node
        # in another word
        # check if this attribute can be generalized to a given hierarchy
        for child in marital_child_list:
            gen = child.check_and_change(marital_info)
            if gen != None:
                marital_info = gen
        for child in race_child_list:
            gen = child.check_and_change(race_info)
            if gen != None:
                race_info = gen
        for child in gender_child_list:
            gen = child.check_and_change(gender_info)
            if gen != None:
                gender_info = gen
        for child in age_child_list:
            gen = child.check_and_change(age_info)
            if gen != None:
                age_info = gen
        # gather quai cluster info,use as dict index
        quai = marital_info+race_info+gender_info+age_info
        if quai in quai_to_number:
            # recode with quai (count++)
            quai_to_number[quai] += 1
            # generate new record 
            # quai_to_number[quai] >= k guarantee records in quai-cluster smaller than k 
            # will be suppressed
            if generalize and quai_to_number[quai] >= k:
                items = record.split(",")
                items[5] = marital_info
                items[8] = race_info
                items[9] = gender_info
                items[0] = age_info
                new_record = items.pop(0) 
                for item in items:
                    new_record += ", "
                    new_record += item
                new_records_list.append(new_record)
            # if count of a quai-cluster reach k record don't need to be suppressed 
            # sup-number-- and generalize all records
            if quai_to_number[quai] == k:
                sup_number -= (k-1)
                for brand_record in quai_to_record[quai]:
                    items = brand_record.split(",")
                    items[5] = marital_info
                    items[8] = race_info
                    items[9] = gender_info
                    items[0] = age_info
                    new_record = items.pop(0) 
                    for item in items:
                        new_record += ", "
                        new_record += item
                    new_records_list.append(new_record)
            elif quai_to_number[quai] < k:
                quai_to_record[quai].append(record)
                sup_number += 1
        # first record in a quai
        else:
            quai_to_record[quai] = [record]
            quai_to_number[quai] = 1
            sup_number += 1 
    if generalize :
        return new_records_list
    # if sup_number > max_sup too many records need to be suppressed
    if sup_number > max_sup:
        return False
    else:
        return True

# used to assist build hierarchy tree of "age" attribute
# (lowerbound,upbound) will be divided by step into several range
def range_sever(lowerbound,upbound,step):
    range_set = []
    low = lowerbound
    up = lowerbound + step - 1
    while up <= upbound:
        range_set.append((low,up))
        low += step
        up += step
    return range_set

# used to assist build hierarchy tree of "age" attribute
# turn (lowerbound,upperbound) into "lowerbound_upperbound"
def range_format(low,up):
    if low == up:
        return str(up)
    else:
        return str(low) + '_' + str(up)

# used to assist build hierarchy tree of "age" attribute
# hier is (step1,step2,step3...,1) step1 > step2 > step3 ...
# (lowerbound,upbound) will first be divided by step1 and then step2 ...
# result will be write in ./K-Anonymity实验数据/adult_date.txt in same format of 
# "adule_gender.txt"
def numer_to_hier(lowerbound,upbound,hier):
    if len(hier) != 0:
        new_range_set = range_sever(lowerbound,upbound,hier[0])
        date_file = open("./K-Anonymity实验数据/adult_date.txt","a")
        for new_range in new_range_set:
            date_file.write(range_format(new_range[0],new_range[1])+","+range_format(lowerbound,upbound)+'\n')
        date_file.close()
        for new_range in new_range_set:
            numer_to_hier(new_range[0],new_range[1],hier[1:])

# write records in new_records_list into new_file_name
def write_new_file(new_file_name,new_records_list):
    new_file = open(new_file_name,"w")
    for record in new_records_list:
        new_file.write(record)
    new_file.close()
        

data = open("./K-Anonymity实验数据/adult.data","r")
# build all generalize tree
race_tree = tree("*")
race_tree.read_and_construct("./K-Anonymity实验数据/adult_race.txt")
marital_status_tree = tree("*")
marital_status_tree.read_and_construct("./K-Anonymity实验数据/adult_marital_status.txt")
gender_tree = tree("*")
gender_tree.read_and_construct("./K-Anonymity实验数据/adult_gender.txt")
age_tree = tree("0_99") 
age_tree.read_and_construct("./K-Anonymity实验数据/adult_date.txt") 
records = data.readlines();

# samarati function
# k = 10,max_sup = 10
low = 0
high = 8 
best_vec = (0,0,0,0)
while low < high:
    mid = (high + low) // 2 + 1
    sati = False
    valid_vecs = valid_vec_gen(high,low)
    for valid_vec in valid_vecs:
        if(sati == True):
            break
        if satisfy(10,10,valid_vec,records,marital_status_tree,race_tree,gender_tree,age_tree):
            sati = True
            low = mid
            best_vec = valid_vec
    if sati != True:
        high = mid -1
# write record list into new_file name
new_file_name = "./K-Anonymity实验数据/new_adult.data"
new_records_list = satisfy(10,10,best_vec,records,marital_status_tree,race_tree,gender_tree,age_tree,True)
write_new_file(new_file_name,new_records_list)
data.close()
