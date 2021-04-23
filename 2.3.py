def mean(seq):
    return float(sum(seq)) / len(seq)

def calculation():

    prompt = "Enter the RUN time : "

    data = []

    count = 0
    while count < 5:
        count += 1
        try:

            value = raw_input(prompt)

            if not value:
                print("Ok Done")
                break

            data.append(float(value))
        except Exception as ex:
            print("Apparently not a number")

    if data:
        msg = "Average of {0} ,over {1} races".format(mean(data)), len(data))
    else:
        msg = "Cannot calculate , data is empty"

    print msg
calc_mean_pace()