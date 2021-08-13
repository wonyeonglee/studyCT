#def solution(participant, completion):
 #   new_participant = participant.copy()
 #   for people in completion:
  #      if (people in new_participant):
 #           new_participant.remove(people)
#
  #  return new_participant[0]
#
#정확성 100 효율성 0

def solution(participant, completion):
    hashtables = {}
    for p in participant:
        if(p in hashtables):
            hashtables[p] +=1
        else:
            hashtables[p] =1
    for p in completion:
        if(p in hashtables):
            hashtables[p]-=1
            if(hashtables[p]==0):
                del hashtables[p]
    for k in hashtables:

    return list(hashtables.keys)[0]
print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))