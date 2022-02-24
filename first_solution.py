fin = open('d_dense_schedule.in.txt', 'r')
fout = open('out.out.txt', 'w')

def first_solution():
    details = list(map(int, fin.readline().split()))
    #print(details)
    contributors_dict = {}
    projects_dict = {}
    for cont in range(details[0]):
        contributor = fin.readline().split()
        #contributors_dict[contributor[0]] = []
        #print(contributors_dict)
        #print(contributor)
        for skil in range(int(contributor[1])):
            skills = fin.readline().split()
            if skil == 0:
                contributors_dict[contributor[0]] = skills
            else:
                contributors_dict[contributor[0]] += skills
            #print(contributors_dict)
            #print(skills)

    for proj in range(details[1]):
        project = fin.readline().split()
        #print(project)

        for rol in range(int(project[4])):
            roles = fin.readline().split()
            if rol == 0:
                projects_dict[project[0]] = roles
            else:
                projects_dict[project[0]] += roles
            #print(projects_dict)
            #print(roles)
    #print(contributors_dict)
    #print(projects_dict)
    return contributors_dict, projects_dict

def assignment(contributors_dict, projects_dict):
    assignment_dict = {}
    project_req = {}
    contributor_have = {}
    contributor_lst = []
    project_lst = []
    for key, value in projects_dict.items():
        #print('key......', key)
        pr = []
        for val in range(0, int(len(value)/1), 2):
            pr.append(value[val])
            #print(pr)
            """if val == 0:
                project_req[key] = value[val]
            else:
                project_req[key] += value[val]"""
        for k, v in contributors_dict.items():
            cn = []
            for a in range(0, int(len(v)/1), 2):
                cn.append(v[a])
                #print(cn)
                """if a == 0:
                    contributor_have[k].append(v[a])
                else:
                    contributor_have[k].append(v[a])"""
            if set(cn).issubset(pr):
                if k == 0:
                    assignment_dict[key] = k
                else:
                    assignment_dict[key] = k
    #print('assingment......',assignment_dict)
    #print(project_req)
    #print(contributor_have)
    #print('project', project_lst)
    #print('contributor', contributor_lst)
    return assignment_dict
def calculating(assignment_dict):
    projects_taken = 0
    projects_taken_list = []
    for ke in assignment_dict.keys():
        projects_taken += 1
    projects_taken = str(projects_taken) + '\n'
    fout.write(str(projects_taken))
    for k, v in assignment_dict.items():
        k = k + '\n'
        v = v+ '\n'
        fout.write(k)
        fout.write(v)
    #print('projects_taken', projects_taken)
    #print('projects_taken_list', projects_taken_list)


contributors_dict, projects_dict = first_solution()
assignment_dict = assignment(contributors_dict, projects_dict)
calculating(assignment_dict)
fin.close()
fout.close()
