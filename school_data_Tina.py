import numpy as np

school_names = {
    1224 : "Centennial High School",
    1679 : "Robert Thirsk School",
    9626 : "Louise Dean School",
    9806 : "Queen Elizabeth High School",
    9813 : "Forest Lawn High School",
    9815 : "Crescent Heights High School",
    9816 : "Western Canada High School",
    9823 : "Central Memorial High School",
    9825 : "James Fowler High School",
    9826 : "Ernest Manning High School",
    9829 : "William Aberhart High School",
    9830 : "National Sport School",
    9836 : "Henry Wise Wood High School",
    9847 : "Bowness High School",
    9850 : "Lord Beaverbrook High School",
    9856 : "Jack James High School",
    9857 : "Sir Winston Churchill High School",
    9858 : "Dr. E. P. Scarlett High School",
    9860 : "John G Diefenbaker High School",
    9865 : "Lester B. Pearson High School"
}

school_codes = [1224, 1679, 9626, 9806, 9813, 9815, 9816, 9823, 9825, 9826, 9829, 9830, 
9836, 9847, 9850, 9856, 9857, 9858, 9860, 9865]

school_years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

grades = [10, 11, 12]

year_2013 = np.array([591, 572, 558,
472,	346,	0,
45,	    57,	    52,
160,	176,	189,
426,	483,	567,
620,	584,	585,
658,	631,	632,
289,	280,	311,
496,	465,	528,
523,	467,	517,
487,	413,	457,
29,	    29,	    45,
399,	361,	380,
210,	225,	359,
657,	566,	501,
163,	146,	228,
587,	611,	648,
514,	577,	522,
435,	364,	509,
504,	530,	512
]).reshape(20,3)

year_2014 = np.array([
599,	592,	598,
444,	452,	341,
40,	    49,	    55,
151,	137,	173,
430,	404,	572,
662,	611,	602,
618,	639,	605,
323,	370,	395,
422,	437,	524,
522,	549,	529,
537,	502,	416,
36,	    44,	    44,
362,	371,	354,
219,	200,	222,
569,	619,	562,
131,	164,	208,
604,	641,	720,
549,	541,	581,
438,	431,	459,
518,	501,	565
]).reshape(20,3)

year_2015 = np.array([
558,	585,	598,
419,	411,	463,
29, 	36,	    68,
137,	115,	106,
373,	403,	532,
659,	643,	583,
624,	610,	594,
271,	227,	316,
564,	383,	455,
565,	530,	543,
469,	491,	499,
48, 	37, 	43,
361,	337,	373,
215,	209,	212,
578,	489,	590,
116,	126,	201,
726,	626,	651,
515,	523,	529,
461,	406,	494,
552,	495,	515
]).reshape(20,3)

year_2016 = np.array([
625,	555,	600,
345,	396,	436,
16,	    47,	    56,
155,	93,	    137,
431,	384,	567,
440,	514,	659,
682,	571,	630,
183,	210,	230,
197,	237,	459,
581,	583,	546,
460,	438,	499,
41,	    46,	    48,
341,	367,	377,
233,	207,	221,
535,	546,	543,
74,	    95,	    179,
691,	740,	680,
556,	528,	568,
420,	456,	511,
459,	512,	564
]).reshape(20,3)

year_2017 = np.array([
611,	617,	582,
433,	374,	450,
15, 	48,	    58,
115,	123,	106,
395,	378,	531,
408,	388,	529,
798,	665,	636,
355,	368,	491,
215,	193,	330,
607,	557,	555,
491,	439,	423,
45,	    50,	    56,
422,	338,	390,
249,	241,	232,
583,	506,	534,
127,	127,	191,
706,	680,	763,
546,	580,	549,
459,	418,	517,
497,	423,	582
]).reshape(20,3)

year_2018 = np.array([
485,	540,	582,
398,	423,	391,
23,	    25,	    58,
150,	83,	    120,
395,	402,	527,
568,	426,	510,
716,	688,	651,
387,	388,	419,
242,	204,	254,
685,	576,	535,
437,	473,	428,
38,	    45,	    57,
417,	391,	398,
386,	238,	249,
229,	250,	495,
81,	    112,	135,
703,	705,	744,
533,	496,	580,
443,	438,	460,
551,	456,	473
]).reshape(20,3)

year_2019 = np.array([
463,	481,	556,
355,	430,	455,
13,	    23,	    52,
146,	146,	127,
383,	397,	441,
556,	615,	530,
723,	724,	798,
391,	391,	409,
251,	234,	322,
674,	692,	629,
476,	447,	507,
61,	    56,	    69,
458,	434,	424,
391,	381,	254,
241,	245,	299,
102,	77,	    146,
749,	677,	744,
488,	514,	503,
474,	449,	531,
535,	528,	553
]).reshape(20,3)

year_2020 = np.array([
455,	436,	437,
360,	352,	437,
12,	    21,	    34,
137,	143,	142,
378,	361,	438,
565,	555,	629,
690,	727,	734,
543,	401,	459,
290,	234,	315,
491,	662,	680,
420,	465,	434,
34, 	59,	    64,
532,	449,	431,
402,	382,	364,
482,	251,	293,
128,	102,	144,
739,	746,	709,
540,	463,	503,
452,	482,	475,
537,	533,	559
]).reshape(20,3)

all_data = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020])

def main():
    print("ENSF 592 School Enrollment Statistics")

    print("Shape of full data array: ", all_data.shape)
    print("Dimensions of full data array: ", all_data.ndim)
    #print(all_data)

    search = True
    while search:
        try:
            input_value = str(input("Please enter the high school name or school code: "))
            for key, value in school_names.items():
                if value == input_value or str(key) == input_value:
                    school_code = key
                    school_name = value
                    search = False
                    break
            else:
                raise ValueError
        except ValueError:
            print("You must enter a valid school name or code.")
    

    school_index = school_codes.index(school_code)
    school_subarray = all_data[::1, school_index, ::1]

    print("\n***Requested School Statistics***\n")
    print("School Name: {0}, School Code: {1}".format(school_name, school_code))
    print("Mean enrollment for Grade 10: ", school_subarray.mean(axis=0)[0])
    print("Mean enrollment for Grade 11: ", school_subarray.mean(axis=0)[1])
    print("Mean enrollment for Grade 12: ", school_subarray.mean(axis=0)[2])
    print("Highest enrollment for a single grade: ", school_subarray.max())
    print("Lowest enrollment for a single grade: ", school_subarray.min())

    for i in range(len(school_years)):
        print("Total enrollment for {0}: {1}".format(school_years[i], school_subarray.sum(axis=1)[i]))

    over_500 = school_subarray[school_subarray > 500]
    if(len(over_500) == 0):
        print("No enrollments over 500.")
    else:
        print("For all enrollments over 500, the median value was: ", np.median(over_500))

    print("\n***General Statistics for All Schools***\n")

    print("Mean enrollment in 2013: ", all_data[0].mean())
    print("Mean enrollment in 2020: ", all_data[7].mean())
    print("Total graduating class of 2020: ", all_data[7].sum(axis=0)[2])
    print("Highest enrollment for a single grade: ", all_data.max())
    print("Lowest enrollment for a single grade: ", all_data.min())

if __name__ == '__main__':
    main()



# Extra
#    for i in range(len(school_years)):
 #       print("Enrollment for {0}: {1} Grade 10, {2} Grade 11, {3} Grade 12".format(school_years[i], school_subarray[i,0], school_subarray[i,1], school_subarray[i,2]))


#    while True:
 #       try:
  #          input_year = int(input("Please enter a valid year between 2013 and 2020: "))
   #         if input_year >= 2013 and input_year <= 2020:
    #            break
     #       else:
      #          raise ValueError
       # except ValueError:
        #    print("Please enter a year between 2013 and 2020.")

