from gui import create_app

root, close_database = create_app()

root.mainloop()

close_database()