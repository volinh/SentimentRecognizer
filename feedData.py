import os

def feed_raw_data(filePath,fileOutputPath):
    data = []
    with open(filePath, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line != "":
                arr = line.split("\t")
                data.append(arr[7].strip())
    write_file(fileOutputPath + filePath.split("/")[1],data)
    return data


def write_file(filePath,data):
    with open(filePath,"w") as file :
        for line in data :
            file.write(line + "\n")


def format_data():
    pass


if __name__ == "__main__" :
    for i in os.listdir("data") :
        fileRawPath = "rawdata/"
        filePath = "data/" + i
        feed_raw_data(filePath,fileRawPath)


