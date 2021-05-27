class tree:
    def __init__(self,data,children = None): 
        self.data = data
        self.children = []
        if(children != None):
            for child in children:
                self.add_children(child)

    def add_children(self,child):
        self.children.append(child)

    def search(self,data):
        if self.data == data:
            return self
        for node in self.children:
            result = node.search(data)
            if result != None:
                return result
        return None

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

    def read_and_construct(self,file_path):
        filename = open(file_path,"r")
        records = filename.readlines()
        for record in records:
            root_data = record.split(",")[1].strip()
            root = self.search(root_data)
            root.add_children(tree(record.split(",")[0]))
        filename.close()

    def get_children(self,depth):
        if depth == 0:
            return [self]
        else:
            child_list = [];
            for child in self.children:
                child_list = child_list + child.get_children(depth - 1)
            return child_list

    def check_and_change(self,attribute):
        if self.search(attribute) != None:
            return self.data
        else:
            return None

def satisfy(max_sup,k,general_level_vec,records,marital_status_tree,race_tree,gender_tree):
    marital_child_list = marital_status_tree.get_children(general_level_vec[0])
    race_child_list = race_tree.get_children(general_level_vec[1])
    gender_child_list = gender_tree.get_children(general_level_vec[2])
    quai_to_number = {}
    sup_number = 0
    for record in records:
        marital_info = record.split(",")[5].strip()
        race_info = record.split(",")[8].strip()
        gender_info = record.split(",")[9].strip()
        
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
        quai = marital_info+race_info+gender_info
        if quai in quai_to_number:
            quai_to_number[quai] += 1
            if quai_to_number[quai] == k:
                sup_number -= (k-1)
            elif quai_to_number[quai] < k:
                sup_number += 1
        else:
            quai_to_number[quai] = 1
            sup_number += 1 
    print(quai_to_number)
    print(sup_number)
    if sup_number > max_sup:
        return False
    else:
        return True


data = open("./K-Anonymity实验数据/adult.data","r")
race_tree = tree("*")
race_tree.read_and_construct("./K-Anonymity实验数据/adult_race.txt")
marital_status_tree = tree("*")
marital_status_tree.read_and_construct("./K-Anonymity实验数据/adult_marital_status.txt")
gender_tree = tree("*")
gender_tree.read_and_construct("./K-Anonymity实验数据/adult_gender.txt")
records = data.readlines();
print(satisfy(10,10,[1,1,1],records,marital_status_tree,race_tree,gender_tree))
data.close()



