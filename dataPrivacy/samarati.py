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

def satisfy(max_sup,k,general_level_vec,records,marital_status_tree,race_tree,gender_tree,age_tree,generalize = False):
    marital_child_list = marital_status_tree.get_children(general_level_vec[0])
    race_child_list = race_tree.get_children(general_level_vec[1])
    gender_child_list = gender_tree.get_children(general_level_vec[2])
    age_child_list = age_tree.get_children(general_level_vec[3])
    quai_to_number = {}
    quai_to_record = {}
    new_records_list = []
    sup_number = 0
    for record in records:
        marital_info = record.split(",")[5].strip()
        race_info = record.split(",")[8].strip()
        gender_info = record.split(",")[9].strip()
        age_info = record.split(",")[0].strip()
        
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
        quai = marital_info+race_info+gender_info+age_info
        if quai in quai_to_number:
            quai_to_number[quai] += 1
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
        else:
            quai_to_record[quai] = [record]
            quai_to_number[quai] = 1
            sup_number += 1 
    if generalize :
        print(len(records),len(new_records_list),sup_number)
        return new_records_list
    if sup_number > max_sup:
        return False
    else:
        return True

def range_sever(lowerbound,upbound,step):
    range_set = []
    low = lowerbound
    up = lowerbound + step - 1
    while up <= upbound:
        range_set.append((low,up))
        low += step
        up += step
    return range_set

def range_format(low,up):
    if low == up:
        return str(up)
    else:
        return str(low) + '_' + str(up)

def numer_to_hier(lowerbound,upbound,hier):
    if len(hier) != 0:
        new_range_set = range_sever(lowerbound,upbound,hier[0])
        date_file = open("./K-Anonymity实验数据/adult_date.txt","a")
        for new_range in new_range_set:
            date_file.write(range_format(new_range[0],new_range[1])+","+range_format(lowerbound,upbound)+'\n')
        date_file.close()
        for new_range in new_range_set:
            numer_to_hier(new_range[0],new_range[1],hier[1:])

def write_new_file(new_file_name,new_records_list):
    new_file = open(new_file_name,"w")
    for record in new_records_list:
        new_file.write(record)
    new_file.close()
        

data = open("./K-Anonymity实验数据/adult.data","r")
race_tree = tree("*")
race_tree.read_and_construct("./K-Anonymity实验数据/adult_race.txt")
marital_status_tree = tree("*")
marital_status_tree.read_and_construct("./K-Anonymity实验数据/adult_marital_status.txt")
gender_tree = tree("*")
gender_tree.read_and_construct("./K-Anonymity实验数据/adult_gender.txt")
age_tree = tree("0_99") 
age_tree.read_and_construct("./K-Anonymity实验数据/adult_date.txt") 
records = data.readlines();

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
new_file_name = "./K-Anonymity实验数据/new_adult.data"
new_records_list = satisfy(10,10,best_vec,records,marital_status_tree,race_tree,gender_tree,age_tree,True)
write_new_file(new_file_name,new_records_list)
data.close()
