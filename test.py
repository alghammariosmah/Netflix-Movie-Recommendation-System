#!/usr/bin/python
# -*- coding: utf-8 -*-


h= open('movie_titles.txt','r')
open_file=h.readlines()
dictionary={}
for line in open_file:
    f=line.split('\n')[0].split('\t')
    for element in f:
        q=element.split(',')
        MovieID, YearOfRelease, Title= q[0],q[1],q[2]
        dictionary.setdefault(MovieID,{})
        dictionary[MovieID]=Title



dictionary1=dict()

lista=[]

for number in xrange(11):

    h= '{0:07}'.format(number)

    files='mv_'+h+'.txt'

    if files not in lista:

        lista.append(files)

del lista[0]

for element in lista:

    with open(element, 'r') as openfile:

        xxx=openfile.read().splitlines()

        Movie_title_semicolon= xxx[0]
        Movie_title= Movie_title_semicolon[:-1]
        open_contents=xxx[1:]


        for x in open_contents:
            a=x.split(",")
            CustomerID,Ranking=a[0],float(a[1])
            dictionary1.setdefault(CustomerID, {})
            dictionary1[CustomerID][Movie_title]=Ranking



critics={}
for customer in dictionary1:
    for movie in dictionary1[customer] or dictionary:
        h=dictionary1[customer]
        j=h.values()[0]
        p= dictionary[movie]
        critics.setdefault(customer,{})
        critics[customer][p]=j


'''
for i in critics:
    if len(critics[i])>4:
        print i,critics[i]
'''
print "Testing :==========================================================================="





# A dictionary of movie critics and their ratings of a small
# set of movies

from math import sqrt

# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs, person1, person2):
    # Get the list of shared_items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]: si[item] = 1

    # if they have no ratings in common, return 0
    if len(si) == 0: return 0

    # Add up the squares of all the differences
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])

    return 1 / (1 + sqrt(sum_of_squares))

#print sim_distance(critics,'1470123','491531')


# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs, p1, p2): #problem : the result always comes 0
    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item] = 1

    # if they are no ratings in common, return 0
    if len(si) == 0: return 0

    # Sum calculations
    n = len(si)


    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])



    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])



    # Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])



    # Calculate r (Pearson score)
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0

    r = num / den

    return r




#print sim_pearson(critics,'873713','1935793')


def sim_jaccard(prefs, genre1, genre2):  # Jaccard Distance (A, B) = |A intersection B| / |A union B|

    # Get the list of shared_items
    p1_intersect_p2 = {}
    for item in prefs[genre1]:
        if item in prefs[genre2]: p1_intersect_p2[item] = 1

    # if they have no items in common, return 0
    if len(p1_intersect_p2) == 0: return 0

    # Get the list of all items that we have
    p1_union_p2 = prefs[genre1]
    for item in prefs[genre2]:
        if item not in p1_union_p2: p1_union_p2[item] = 1

    #Get the total number of items for intersection and union
    p1_intersect_p2, p1_union_p2 = len(p1_intersect_p2), len(p1_union_p2)

    return float(p1_intersect_p2) / float(p1_union_p2) # return jaccard distance

#print sim_jaccard(critics,'1461435','946156')


def sim_jaccard2(prefs, genre1, genre2):

    #Get the list of items
    genre1_movies = prefs[genre1].keys()
    genre2_movies = prefs[genre2].keys()

    # Make them sets in order to be able to use built-in methods of it such as intersection and union
    p1, p2 = set(genre1_movies), set(genre2_movies)
    p1_intersect_p2 = p1.intersection(p2)
    p1_union_p2 = p1.union(p2)

    #Get the total number of items for intersection and union
    p1_intersect_p2, p1_union_p2 = len(p1_intersect_p2), len(p1_union_p2)

    # if they have no items in common, return 0
    if p1_intersect_p2 == 0: return 0

    return float(p1_intersect_p2) / float(p1_union_p2) # return jaccard distance

#print sim_jaccard2(critics,'1828803','1664010')

# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]
#print topMatches(critics,'1213178',5,sim_pearson)



# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs, person, similarity=sim_pearson):#probelms does not recommend anything LOL
    totals = {}
    simSums = {}
    for other in prefs:
        # don't compare me to myself
        if other == person: continue
        sim = similarity(prefs, person, other)

        # ignore scores of zero or lower
        if sim <= 0: continue
        for item in prefs[other]:

            # only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # Create the normalized list
    rankings = [(total / simSums[item], item) for item, total in totals.items()]

    # Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings
#print getRecommendations(critics,'1213178',sim_distance)



def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            # Flip item and person
            result[item][person] = prefs[person][item]
    return result

#print transformPrefs(critics)


def calculateSimilarItems(prefs, n=10):
    # Create a dictionary of items showing which other items they
    # are most similar to.
    result = {}
    # Invert the preference matrix to be item-centric
    itemPrefs = transformPrefs(prefs)
    c = 0
    for item in itemPrefs:
        # Status updates for large datasets
        c += 1
        if c % 100 == 0: print "%d / %d" % (c, len(itemPrefs))
        # Find the most similar items to this one
        scores = topMatches(itemPrefs, item, n=n, similarity=sim_distance)
        result[item] = scores
    return result

#print calculateSimilarItems(critics,10)



def getRecommendedItems(prefs, itemMatch, user):
    userRatings = prefs[user]
    scores = {}
    totalSim = {}
    # Loop over items rated by this user
    for (item, rating) in userRatings.items():

        # Loop over items similar to this one
        for (similarity, item2) in itemMatch[item]:

            # Ignore if this user has already rated this item
            if item2 in userRatings: continue
            # Weighted sum of rating times similarity
            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating
            # Sum of all the similarities
            totalSim.setdefault(item2, 0)
            totalSim[item2] += similarity

    # Divide each total score by total weighting to get an average
    rankings = [(score / totalSim[item], item) for item, score in scores.items()]

    # Return the rankings from highest to lowest
    rankings.sort()
    rankings.reverse()
    return rankings
itemsim= calculateSimilarItems(critics)
#print getRecommendedItems(critics,itemsim,'1828803')

#print getRecommendations(critics,'643182',sim_distance)
#print getRecommendedItems(critics,itemsim,'643182')

while True:
    Quest=raw_input("\nSelect a number or done to end:\n 1- User recommendation \n 2- Item recommendation\n")
    if Quest == '1':
        ID= raw_input("from above, Insert the user ID to recommend him a movie 'user-based':\n")
        try:
            recommended= getRecommendations(critics,'%s'%ID,sim_distance)
            print "Recommended movies with the ratings are:\n",recommended
        except:
            print "rewrite the ID correctly please"
    elif Quest == '2':
        Item= raw_input("from above select the User ID to recommend him a movie according 'item-based':\n")
        try:
            recommended=getRecommendedItems(critics,itemsim,'%s'%Item)
            print 'Recommended movies with the ratings are:\n',recommended
        except:
            print "rewrite the ID correctly please"
    elif Quest == 'done':
        break
    else:
        print "please try again"
