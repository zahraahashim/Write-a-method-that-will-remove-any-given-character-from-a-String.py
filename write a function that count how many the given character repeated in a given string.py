import collections

def charcount(string):
    results = collections.Counter(string)
    print(results)
    return results


the_string = "vnkw2nfijgmbrjgjgj40jgirjeivjiegiejgjegewgjokjgokeorgjkrjkg945j9"
charcount(the_string)
