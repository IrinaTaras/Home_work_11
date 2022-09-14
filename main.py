from flask import Flask, render_template
import utils


app = Flask(__name__)
@app.route("/")

def page_candidates():
    candidates = utils.load_candidates_from_json()
    return render_template('all_candidates.html', candidates=candidates)

@app.route("/candidate/<int:can_id>")
def page_candidate(can_id):
    candidate = utils.get_candidate(can_id)
    return render_template('card.html', candidate=candidate)

@app.route("/search/<candidate_name>")
def page_candidates_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))

@app.route("/skill/<skill_name>")
def page_candidates_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, skill_name=skill_name, count_candidates=len(candidates))




app.run()
