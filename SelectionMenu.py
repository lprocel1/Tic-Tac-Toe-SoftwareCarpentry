
def Selection():
    """
    Initial startup window for game configuration.

    Returns
    -------
    list
        Returns key values: size: *int* for the dimensions of the game board.
                            comp.get(): *str* to indicate playing status

    """
    import tkinter as tk

    def clickSize(var):
        global size
        size = var.get()

    def clickBool(boolvar):
        global compBool
        compBool = boolvar.get()
        return compBool

    def submit():
        selection.destroy()

    def toggleComp(frame, comp):
        if comp.get() == "Two-Player":
            comp.set("Single Player")

            tk.Label(frame, text="Single Player Mode").grid(
                row=5, column=1, columnspan=4
            )
        else:
            comp.set("Two-Player")

            tk.Label(frame, text=" Two Player Mode ").grid(
                row=5, column=1, columnspan=4
            )

    selection = tk.Tk()
    selection.title("selection menu")
    selection.resizable(width=False, height=False)
    frame = tk.Frame(selection)
    frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
    tk.Grid.rowconfigure(frame, 0, weight=1)
    tk.Grid.columnconfigure(frame, 1, weight=1)
    tk.Label(frame, text="welcome to tic tac toe!").grid(
        row=0, column=1, columnspan=2, sticky=tk.N + tk.E + tk.S + tk.W
    )
    boolvar = tk.BooleanVar()
    var = tk.IntVar()

    tk.Label(frame, text=" ----- Single or Multiplayer game -----").grid(
        row=2, column=0, columnspan=4, sticky=tk.N + tk.E + tk.S + tk.W
    )
    tk.Label(frame, text="(Default: Two Player)").grid(
        row=3, column=0, columnspan=4, sticky=tk.N + tk.E + tk.S + tk.W
    )
    comp = tk.StringVar()
    comp.set("Two-Player")
    b1 = tk.Button(
        frame, textvariable=comp, command=lambda comp=comp: toggleComp(frame, comp)
    ).grid(row=4, column=1, columnspan=4, sticky=tk.N + tk.S + tk.E + tk.W)

    tk.Label(frame, text=" ----- please select a board size -----").grid(
        row=6, column=0, columnspan=4, sticky=tk.N + tk.E + tk.S + tk.W
    )

    s1 = tk.Radiobutton(
        frame,
        text="3x3 board",
        variable=var,
        value=3,
        command=lambda var=var: clickSize(var),
    )
    s1.grid(row=7, column=1, columnspan=3)
    s2 = tk.Radiobutton(
        frame,
        text="4x4 board",
        variable=var,
        value=4,
        command=lambda var=var: clickSize(var),
    )
    s2.grid(row=8, column=1, columnspan=3)
    s3 = tk.Radiobutton(
        frame,
        text="5x5 board",
        variable=var,
        value=5,
        command=lambda var=var: clickSize(var),
    )
    s3.grid(row=9, column=1, columnspan=3)
    submitbtn = tk.Button(frame, text="Submit", command=submit).grid(row=11, column=1)
    selection.mainloop()

    return [size, comp.get()]


if __name__ == "__main__":
    sized = Selection()
    print(sized)
