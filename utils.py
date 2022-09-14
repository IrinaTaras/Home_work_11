import json

def load_candidates_from_json():

    with open("candidates.json", 'rt', encoding="utf-8") as file:
        return json.loads(file.read())


def get_candidate(pk):
    for candidate in load_candidates_from_json():
        if pk == candidate['id']:
            return candidate

def get_candidates_by_name(candidate_name):
    name = candidate_name.lower()
    list_candidates_name = []
    for candidate in load_candidates_from_json():
        if name in candidate['name'].lower():
            list_candidates_name.append(candidate)
    return list_candidates_name


def get_candidates_by_skill(skill_name):
    matching_skills = []
    skill = skill_name.lower()
    for candidate in load_candidates_from_json():
        list_skills = candidate["skills"].lower().split(', ')
        if skill in list_skills:
            matching_skills.append(candidate)
    return matching_skills
