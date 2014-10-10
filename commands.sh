# get number of lines in the file (it's the first result)
wc filename

# get only the first 1000 lines and save them to a new file
head -n 1000 filename > new_filename

sort -R train.libsvm | head -n 4000 > train40.txt

sort -R test.libsvm | head -n 1000 > test1000.txt

time ./svm-train -s 0 -t 1 -d 3 -q libsvm-converter-script/train.libsvm

time ./svm-train -s 0 -t 1 -d 3 -q libsvm-converter-script/train10.libsvm

time ./svm-predict libsvm-converter-script/test10.libsvm train10.libsvm.model output10.txt

./svm-train -s 0 -t 1 -d 3 -q libsvm-converter-script/train.libsvm; ./svm-predict libsvm-converter-script/test.libsvm train.libsvm.model output.txt
