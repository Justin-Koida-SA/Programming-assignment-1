import hw1
import unittest
import data


class TestCases(unittest.TestCase):
    #method must start with 'test' in order for the unittest tests to work ****
    def test_vowel_count1(self):
        vowel = hw1.vowel_count("Jimmy is going to school")
        self.assertEqual(vowel, 7)

    def test_vowel_count2(self):
        vowel = hw1.vowel_count("Why is the sky going upwards")
        self.assertEqual(vowel, 6)

    def test_short_lists1(self):
        short = hw1.short_lists([[6],[8,7],[5,9,10,5,4],[8,5],[10,1]])
        self.assertEqual (short, [8,7,8,5,10,1])

    def test_short_lists2(self):
        short = hw1.short_lists([[10,5,8],[5,4],[9,2],[2]])
        self.assertEqual (short, [5,4,9,2])

    def test_ascending_pairs1(self):
        ascend = hw1.ascending_pairs([[6],[8,7],[5,9,10,5,4],[8,5],[10,1]])
        self.assertEqual (ascend, [6,7,8,5,9,10,5,4,5,8,1,10])

    def test_ascending_pairs2(self):
        ascend = hw1.ascending_pairs([[10,5,8],[5,4],[9,2],[2]])
        self.assertEqual (ascend, [10,5,8,4,5,2,9,2])

    def test_add_prices1(self):
        add = hw1.add_prices(data.Price(5,89),data.Price(9,28))
        self.assertEqual(add, data.Price(15, 17))

    def test_add_prices2(self):
        add = hw1.add_prices(data.Price(3, 33), data.Price(8, 70))
        self.assertEqual(add, data.Price(12, 3))
    #note: accidentally wrote code taking any 2 points, forgot it was top left and bottom right.
    #Although it still should work just had a bunch of unesseary lines accounting for if given random points.
    def test_rect_area1(self):
        point1 = data.Point(6, -10)
        point2 = data.Point(-5, 10)
        rect1 = (data.Rectangle(point1, point2))
        rect = hw1.rectangle_area(rect1)
        self.assertEqual(rect, 220)

    def test_rect_area2(self):
        point1 = data.Point(3, -4)
        point2 = data.Point(8, 10)
        rect1 = (data.Rectangle(point1, point2))
        rect = hw1.rectangle_area(rect1)
        self.assertEqual(rect, 70)

    def test_rect_area3(self):
        point1 = data.Point(-5, -2)
        point2 = data.Point(-1, -8)
        rect1 = (data.Rectangle(point1, point2))
        rect = hw1.rectangle_area(rect1)
        self.assertEqual(rect, 24)

    def test_books_by_authors1(self):
        book1 = data.Book('Justin Koida', 'Healing')
        book2 = data.Book('Quinn Potter', 'Gym')
        book3 = data.Book('Brayden Noguchi', 'Biking')
        book4 = data.Book('Justin Koida', 'Coding')
        book5 = data.Book('Sammy Paykel', 'Rapping')
        book6 = data.Book('Nick Rubel', 'Capping')
        book7 = data.Book('Quinn Potter', 'Sorcery')
        book8 = data.Book('Nick Rubel', 'Basketball')
        book9 = data.Book('Justin Koida', 'Math')
        book10 = data.Book('Quinn Potter', 'Sleep')
        books = [book1,book2,book3,book4,book5,book6,book7,book8,book9,book10]
        author_test = hw1.books_by_author('Justin Koida', books)
        self.assertEqual(author_test, ['Healing', 'Coding', 'Math'])

    def test_books_by_authors2(self):
        book1 = data.Book('Justin Koida', 'Healing')
        book2 = data.Book('Quinn Potter', 'Gym')
        book3 = data.Book('Brayden Noguchi', 'Biking')
        book4 = data.Book('Justin Koida', 'Coding')
        book5 = data.Book('Sammy Paykel', 'Rapping')
        book6 = data.Book('Nick Rubel', 'Capping')
        book7 = data.Book('Quinn Potter', 'Sorcery')
        book8 = data.Book('Nick Rubel', 'Basketball')
        book9 = data.Book('Justin Koida', 'Math')
        book10 = data.Book('Quinn Potter', 'Sleep')
        books = [book1,book2,book3,book4,book5,book6,book7,book8,book9,book10]
        author_test = hw1.books_by_author('Quinn Potter', books)
        self.assertEqual(author_test, ['Gym', 'Sorcery', 'Sleep'])

    def test_circle1(self):
        rect = (data.Rectangle(data.Point(-8,5),data.Point(-2,3)))
        circle = hw1.circle_bound(rect)
        self.assertEqual(circle, data.Circle((-5.0, 4.0), 3.1622776601683795))

    def test_circle2(self):
        rect = (data.Rectangle(data.Point(1,10),data.Point(37,2)))
        circle = hw1.circle_bound(rect)
        self.assertEqual(circle, data.Circle((19, 6), 18.439088914585774))

    def test_pay1(self):
        emp1 = data.Employee('Justin', 50)
        emp2 = data.Employee('Koida', 60)
        emp3 = data.Employee('Quinn', 100)
        emp4 = data.Employee('Potter', 40)
        emp5 = data.Employee('Brayden', 200)
        emp6 = data.Employee('Nick', 65)
        emp7 = data.Employee('Sammy', 73)
        emp8 = data.Employee('Hunter', 43)
        emp9 = data.Employee('Tyler', 38)
        emp10 = data.Employee('Michael', 52)
        emp = [emp1,emp2,emp3,emp4,emp5,emp6,emp7,emp8,emp9,emp10]
        avg = hw1.below_pay_average(emp)
        self.assertEqual(avg, ['Justin','Koida','Potter','Nick','Hunter','Tyler','Michael'])

    def test_pay2(self):
        emp1 = data.Employee('Justin', 550)
        emp2 = data.Employee('Koida', 160)
        emp3 = data.Employee('Quinn', 180)
        emp4 = data.Employee('Potter', 400)
        emp5 = data.Employee('Brayden', 230)
        emp6 = data.Employee('Nick', 650)
        emp7 = data.Employee('Sammy', 373)
        emp8 = data.Employee('Hunter', 243)
        emp9 = data.Employee('Tyler', 348)
        emp10 = data.Employee('Michael', 652)
        emp = [emp1,emp2,emp3,emp4,emp5,emp6,emp7,emp8,emp9,emp10]
        avg = hw1.below_pay_average(emp)
        self.assertEqual(avg, ['Koida','Quinn','Brayden','Sammy','Hunter','Tyler'])

if __name__ == '__main__':
    unittest.main()