# ChatGPT로 생성한클래스.py

# Person 클래스
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        #f-string:변수명을 바로 넘김(포맷 스트링)
        print(f"[Person] ID: {self.id}, Name: {self.name}")


# Manager 클래스 (Person 상속)
class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"[Manager] ID: {self.id}, Name: {self.name}, Title: {self.title}")


# Employee 클래스 (Person 상속)
class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"[Employee] ID: {self.id}, Name: {self.name}, Skill: {self.skill}")


# ----------------------------
# ✅ 테스트 코드 10개
# ----------------------------
def run_tests():
    print("1. Person 테스트")
    p1 = Person(1, "Alice")
    p1.printInfo()

    print("\n2. Manager 테스트")
    m1 = Manager(2, "Bob", "Project Manager")
    m1.printInfo()

    print("\n3. Employee 테스트")
    e1 = Employee(3, "Charlie", "Python")
    e1.printInfo()

    print("\n4. Manager 여러명 테스트")
    m2 = Manager(4, "Diana", "HR Manager")
    m2.printInfo()

    print("\n5. Employee 여러명 테스트")
    e2 = Employee(5, "Eve", "Data Analysis")
    e2.printInfo()

    print("\n6. Manager의 메서드 오버라이딩 확인")
    if hasattr(m1, 'printInfo'):
        m1.printInfo()

    print("\n7. Employee의 메서드 오버라이딩 확인")
    if hasattr(e1, 'printInfo'):
        e1.printInfo()

    print("\n8. Person 리스트 관리")
    people = [p1, m1, e1, m2, e2]
    for person in people:
        person.printInfo()

    print("\n9. ID와 이름 검증")
    assert p1.id == 1 and p1.name == "Alice"
    assert m1.title == "Project Manager"
    assert e1.skill == "Python"
    print("검증 통과")

    print("\n10. isinstance 검증")
    assert isinstance(m1, Person)
    assert isinstance(e1, Person)
    assert not isinstance(p1, Manager)
    print("상속 구조 확인 완료")


# 테스트 실행
run_tests()
