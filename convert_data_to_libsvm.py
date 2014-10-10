print "Convert data to SVM"

TRAIN_SET_PATH = "../Webscope_R4/ydata-ymovies-user-movie-ratings-train-v1_0.txt"
TEST_SET_PATH = "../Webscope_R4/ydata-ymovies-user-movie-ratings-test-v1_0.txt"

MAXIMUM_VALUE = 5.0

def export_dataset_to_libsvm_format( filename ):
    print "Converting", filename.split( "/" )[-1]

    OUTPUT_PATH = filename.split( "/" )[-1] + ".libsvm"

    ratings = {}

    with open( filename , "r") as in_file:
        lines = in_file.readlines()
        for line in lines:
            user_id, movie_id, _, rating = line.split("\t")

            # map values to [0..1]
            rating = float( rating ) / MAXIMUM_VALUE
            rating = str( float("{0:.2f}".format( rating ) ) )

            ratings.setdefault( movie_id, [] )
            ratings[ movie_id ].append( user_id + ":" + rating )

    with open( OUTPUT_PATH , "w") as out_file:
        keylist = ratings.keys()
        keylist.sort()

        for key in keylist:
            out_file.write( key + " " + " ".join( ratings[ key ] ) + "\n" )

if __name__ == "__main__":
    export_dataset_to_libsvm_format( TRAIN_SET_PATH )
    export_dataset_to_libsvm_format( TEST_SET_PATH )