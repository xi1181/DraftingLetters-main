namelist = []
with open ("./contacts/names.txt", "r") as names_file:
    for name in names_file:
        name = name.strip()
        namelist.append(name)
with open ("./Email/draft.txt", "r") as draft_file:
    draft = draft_file.read()

for name in namelist:
    currdraft = draft
    currdraft = currdraft.replace("[name]", name)
    with open(f"./Send/Letter_for_{name}.txt", "w") as letter:
        letter.write(currdraft)