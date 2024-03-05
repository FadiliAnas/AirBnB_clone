import cmd

class HBNBCommand(cmd.Cmd):
    prompt = " (hbnb) "
    def do_quit(self, arg):
       return True
    def do_EOF(self, arg):
        print("\n")
        return True
    # def help_exit(self):
        # print ("Exit the interpreter.")
    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program")
    def do_create(self,arg):
        if arg == "":
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

if __name__ == '__main__':
 HBNBCommand().cmdloop()
