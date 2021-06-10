import csv


class Tempa:
    def seoula(self):
        f = open('D:\\OPENEG\\FT\\PycharmProjects\\js\\ta.csv');
        # f = open('C:\\PycharmProjects\\js\\ta.csv');
        data = csv.reader(f);
        header = next(data);
        tempa = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        # for i in range(10):
        #     tempa.append(0);
        for row in data:
            for i in range(2010, 2021):
                if i == int(row[0].split('-')[0]):
                    tempa[i - 2010] += float(row[2]);

        for i in range(0, len(tempa)):
            tempa[i] = tempa[i] / 365;

        print(tempa);

    def seoulam(self,year, month):
        f = open('D:\\OPENEG\\FT\\PycharmProjects\\js\\ta.csv');
        # f = open('C:\\PycharmProjects\\js\\ta.csv');
        data = csv.reader(f);
        header = next(data);
        htemp = [];
        ltemp = [];
        # for i in range(10):
        #     tempa.append(0);
        for row in data:
            if year == int(row[0].split('-')[0]) and month == int(row[0].split('-')[1]):
                ltemp.append(row[3]);
                htemp.append(row[4]);
        result = [{'low':ltemp},{'high':htemp}];
        #print('low: ',ltemp);
        #print('high: ',htemp);
        return result;




if __name__ == '__main__':
    #Tempa().seoula();
    tempa = Tempa().seoulam(2020,1);
    print(tempa);