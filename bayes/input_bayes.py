"""Data preprocessing for adult dataSet."""

data_url = '../data/adult.data'

def ConvertData(line):
    """Convert the original values of all attributes into an info array
    Args:
        line:the input string that is need to be handled
    Returns:
        a list of the handled strings,if the line contains'?' return None
    """
    if('?' in line):
        return None
    else:
        try:
            line = line[:-1] # remove the char'\n'
            infos = line.split(',' + ' ')
            age = int(infos[0]) / 10  # age
            age = 6 if age > 6 else age
            work = infos[1]  # workclass
            fnlwgt = int(infos[2]) / 100000  # final weight
            fnlwgt = 5 if fnlwgt > 5 else fnlwgt
            edu = infos[3]  # education level
            edu_yrs = int(infos[4]) / 10  # eduacation years
            martial = infos[5]  # martial status
            occup = infos[6]  # occupation
            relat = infos[7]  # relationship
            race = infos[8]  # race
            sex = infos[9]  # sex
            gain = int(infos[10])  # captial gain
            gain = 1 if gain > 0 else gain
            loss = int(infos[11])  # captial loss
            loss = 1 if loss > 0 else loss
            hour = int(infos[12]) / 10  # hours per week
            hour = 5 if hour > 5 else hour
            label = (1 if infos[14] == ">50K" else 0)  # label 1 represents >50k, label 0 represents <= 50k
            return [age, work, fnlwgt, edu, edu_yrs, martial, occup, relat, race, sex, gain, loss, hour, label]
        except:
            return None

def Input():
  """Description.
  Args:
      No args
  Returns:
      A data dict
  """

  #Build a data_dict to count the number of each attribute with the label 0 and label 1
  data_dict = {0:[],1:[]}

  # Count the total number of the samples with label 0 and label 1
  total_num = [0,0]
  for i in range(14):
      data_dict[0].append({})
      data_dict[1].append({})

  with open(data_url,'r') as fi:
    lines = fi.readlines()
    for line in lines:

        # Get te attributes info array.
        infos = ConvertData(line)
        if infos == None:
            continue
        #Count the total number of different labels.
        label = infos[13]
        total_num[label] += 1

        #Count the number of each attribute with the label 0 and label 1
        for i in range(13):
            info = infos[i]
            if(info in data_dict[label][i]):
                num = int(data_dict[label][i][info]) + 1
                data_dict[label][i][info] = num
            else:
                data_dict[label][i][info] = 1
  return data_dict,total_num
