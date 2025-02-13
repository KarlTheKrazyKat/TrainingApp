Very dependent on WINWOM

PYWOM is running off tkinter and python

for tkinter documentation => https://tkdocs.com/
for many frames => https://stackoverflow.com/questions/66470340/how-to-work-on-tkinter-code-and-split-in-multiple-files

VARIABLE NAMING SCHEME 
Majority of variables are now controlled by the naming scheme

textvariables:
    tkinter labels use textvariables to auto-update when the variable is modified
    all text variables are initializes as textvar = StringVar()
    all text variables use .set() and .get() for their values
    -must not be 4 characters to avoid conflicts with functions in pywomlib
    -this comment is likely irrelevent since offloading pywomlib to subclasses
    hence: an = StringVar(value=<some text>)
        &: an.set(<some text>)
        &: print(an.get())

dictionaries:
    <<most dictionaries are no longer used in favor of LRF or DAQ class objects>>
    PYWOM used a lot of dictionaries found from part names to search
    some dictionaries are initialized at the top of the code, 
        but some are initialzed from pywomlib functions later in the code
        -in this case they are usually called from a variable such as an, pn, ps, or pf
    -all dictionaries should be in the format <dictionary name>_d
    hence: an_d = read_whole_record(paths[cfp]['pndata']+an+".LRF")

tkinter frames:
    tkinter frames can be initialized from WINWOM, see WINWOM/README.txt for details
    f_<frame name>


tkinter blocks: 
    these are all defined under VISUAL ELEMENTS
    there are two types of ttk.Label() in use
    static label: 
        these blocks display static text
        normally these have a matching dynamic label and textvariable
    dynamic label:
        these blocks display dynamics information based on textvariables
        these will always have a matching textvariable
    ttk.Entry():
        these blocks accept keyboard input
        these will always have a matching textvariable
        -use .trace_add() to update thise variable

    formats for blocks:
    static label - v_<name>
    dynamic label - vr_<name>
    ttk.Entry() - vi_<name>
    textvariable - <name>

    NOTE: in cases where an entry and a dynamic label exist for the name info, a new textvariable should be created
    hence: an = StringVar()
        &: an_ds = StringVar()
        &: v_an = ttk.Label(content,text="Asset#")
        &: vi_an = ttk.Entry(content,textvariable=an)
        &: vr_an_ds = ttk.Label(content,textvariable=an_ds)

file structure:
    the file structure is very important to VISWOM which is an integral part of PYWOM
    every screen should have a <screen>.py, Screens/<screen>, modules/<screen>, and if it has images an images/<screen>
    if created using WINWOM a screen should autogenerate all of these
    
    this structure allows VISWOM to automatically stitch.py which setups screen elements from the template
    and patch.py which links a <screen>.py to its modules and screen elements

    <screen>/Menus is not as incorporated as i would like yet