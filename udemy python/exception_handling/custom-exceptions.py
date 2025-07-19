
class TereBhaiKiJai(Exception):
    # Exception.with_traceback = "Tere bhai ki jai exception"
    pass
def order(item):
    if item == "unknown":                                       # Code that can through error
        raise TereBhaiKiJai("Sahi item daal dalle!")
    print(f"Order for {item} processed successfully.")

order("unknown")
