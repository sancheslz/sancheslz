import json


class Education:
    def __init__(self, course, institution, year):
        self.course = course
        self.institution = institution
        self.year = year

    def description(self):
        return f"{self.course} - {self.institution} - {self.year}"


class Profile:
    def __init__(self, name, github):
        self.name = name
        self.github = github
        self._education = []
        self._skills = []
        self._interests = []
    
    @property
    def github_profile(self):
        return f"https://github.com/{self.github}"

    def education(self, course):
        self._education.append(course)

    def skills(self, skill):
        self._skills.append(skill)

    def interests(self, interests):
        self._interests.append(interests)
    
    def about(self):
        print(f"👨 {self.name}")
        print(f"🌐 Perfil: {self.github_profile}")

        print(f"\n🎓 Formação:")
        for e in self._education:
            print(f"  - {e.description()}")
            
        print("\n🛠️  Habilidades:")
        for s in self._skills:
            print(f"  - {s}")

        print("\n🤩 Interesses:")
        for i in self._interests:
            print(f"  - {i}")


me = Profile('Lucas Sanches', 'sancheslz')

details = open('details.json').read()
details = json.loads(details)

for category, attributes in details.items():
    for attribute in attributes:
        if category.capitalize() in locals():
            category_obj = locals()[category.capitalize()](*attribute.values())
            me.__getattribute__(category)(category_obj)
        else:
            me.__getattribute__(category)(attribute)

me.about()
