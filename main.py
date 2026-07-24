
class Book:
  def __init__(self,book_id,title,author,category):
     self.book_id = book_id
     self.title = title
     self.author = author
     self.category = category
     self.status = "Available"

class Library:
    def add_book(self):
        books_id = int(input("Enter the Book ID:"))
        title = input("Enter the Title Book:")
        author = input("Enter the Book Author:")
        category = input("Enter the Categoery Book :")

        book = Book(books_id, title, author, category)

        with open("books.txt", "a") as file:
            file.write(f"{book.book_id},{book.title},{book.author},{book.category},{book.status}\n")
        print("Book added successfully!")  
         
    def view_book(self):
         print("Your library Books List")
         try:
             with open("books.txt", "r") as file:
                data = file.readlines()

             if len(data) == 0:
               print("Library List is empty!!!!")
             else:
              for index, line in enumerate(data, 1):
                  try:
                      books_id,title,author,category,status = line.strip().split(",")
                      print(f"{index}.Books id: {books_id}, Title: {title}, Author: {author}, category:{category},status:{status}")
                  except ValueError:
                     print(f"Error in line {index}: {line.strip()}")
         except FileNotFoundError:
           print("No books found. Please add a book first.")

    def search_book(self):
          try:
             with open("books.txt", "r") as file:
                  data = file.readlines()
  
             if len(data) == 0:
               print("No Books Available")
             else:
                self.view_book()
                search_name = input("Enter the name of book in library :")
                found_book = []
                for index, line in enumerate(data, 1):
                  try:
                      books_id,title,author,category,status = line.strip().split(",")
                      if search_name.lower() in title.lower():
                         found_book.append((index,books_id,title,author,category,status)) 
                  except ValueError:
                    print(f"Error in line {index}: {line.strip()}")
                if found_book:
                  print("Search Results:")
                  for index, books_id,title,author,category,status in found_book:
                     print(f"{index}.Books id: {books_id}, Title: {title}, Author: {author},category:{category},status:{status}")
                else:
                     print(f"No books found with the name '{search_name}'.")
          except ValueError:
              print("error in value")
          except FileNotFoundError:
               print("No Books found. Please add a Book first.")  

                      
    def issue_book(self):
        try:
           with open("books.txt", "r") as file:
                data = file.readlines()

           if len(data) == 0:
             print("No Books Available")
           else:
               self.view_book()
               book_id = input("Enter the Book name to be issued:")             
               updated_data=[]
               found = False
               for line in data:
                  books_id,title,author,category,status = line.strip().split(",")
                  if books_id == book_id:
                       found = True
  
                       if status == "Available":
                          status = "Issued"
                          print(f"'{title}' issued successfully.")
                       else:
                          print(f"{title} Books is already issued")
                  
                  updated_data.append(f"{books_id},{title},{author},{category},{status}\n")
               if not found:
                      print("Book ID not found.")
          
               with open("books.txt", "w") as file:
                      file.writelines(updated_data)        
                            
 
        except ValueError:
             print("No Books found. Please add a Book first.")      
    
             
    def return_book(self):
          try:
              with open("books.txt", "r") as file:
                   data = file.readlines()
    
              if len(data) == 0:
                print("No Books Available")
                return 
              self.view_book()
              book_id = input("Enter the Book ID to Return Book: ")

              updated_data=[]
              found = False

              for line in data:
                  books_id,title,author,category,status = line.strip().split(",")

                  if books_id == book_id:
                       found = True
                       if status == "Issued":
                          status = "Available"

                          print(f"'{title}' returned successfully.")
                       else:
                          print(f"'{title}' is already available.")
                  updated_data.append(f"{books_id},{title},{author},{category},{status}\n")
                        
              with open("books.txt", "w") as file:
                    file.writelines(updated_data)
          except FileNotFoundError:
            print("No Books found. Please add a Book first.")        
          except ValueError:
               print("No Books found. Please add a Book first.")  
           

    
    def delete_book(self):
        try:
             with open("books.txt", "r") as file:
                  data = file.readlines()
               
             if len(data) == 0:
                 print("Library List is empty!!!!")
                 return
             
             self.view_book()

             search_index = int(input("enter the book number delete: "))-1
             
             if 0 <= search_index < len(data):
                 remove_book = data.pop(search_index)

                 with open("books.txt", "w") as file:
                     file.writelines(data)

                 print(f"remove books:{remove_book.strip()}.")
             else:
                 print("invalid book number")
        except ValueError:
            print("Please enter a valid book number.")
        except FileNotFoundError:
           print("No books found. Please add a books first.")


library = Library()
while True:
  print("===== LIBRARY MANAGEMENT SYSTEM =====")
  print("1. Add Book")
  print("2. View Books")
  print("3. Search Book")
  print("4. Issue Book")
  print("5. Return Book")
  print("6. Delete Book")
  print("7. Exit")
  choice = input("Enter the choice management:")
  if choice == "1":
       library.add_book()
  elif choice == "2":
       library.view_book()
  elif choice == "3":
       library.search_book()
  elif choice == "4":
       library.issue_book()
  elif choice == "5":
       library.return_book()
  elif choice == "6":
       library.delete_book()
  elif choice == "7":
       print("Exit the library management system !!")
       break