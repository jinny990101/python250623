class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"[Person] ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"[Manager] ID: {self.id}, Name: {self.name}, Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"[Employee] ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 코드 10개
def run_tests():
    print("1. Person 인스턴스 생성 및 출력")
    p = Person(1, "Alice")
    p.printInfo()

    print("\n2. Manager 인스턴스 생성 및 출력")
    m = Manager(2, "Bob", "Team Lead")
    m.printInfo()

    print("\n3. Employee 인스턴스 생성 및 출력")
    e = Employee(3, "Charlie", "Python")
    e.printInfo()

    print("\n4. Manager의 title 확인")
    assert m.title == "Team Lead"

    print("\n5. Employee의 skill 확인")
    assert e.skill == "Python"

    print("\n6. Person 상속 확인 (Manager)")
    assert isinstance(m, Person)

    print("\n7. Person 상속 확인 (Employee)")
    assert isinstance(e, Person)

    print("\n8. Manager 오버라이드 메서드 확인")
    m.printInfo()

    print("\n9. Employee 오버라이드 메서드 확인")
    e.printInfo()

    print("\n10. 여러 객체 리스트 출력")
    people = [p, m, e]
    for person in people:
        person.printInfo()