"""
Defines the skeleton of a base algorithm, deferring definition of exact
steps to subclasses.
"""

# format file

def get_text(): return "plain-text"
def get_pdf(): return "pdf"
def get_csv(): return "csv"

# converter and save operation

def convert_to_text(data):
    print("[CONVERT]")
    return f"{data} as text"
def saver():
    print("[SAVE]")


# template

def template_function(getter, converter=False, to_save=False):
    data = getter()
    print(f"Got `{data}`")

    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        print("Skip conversion")

    if to_save:
        saver()

    print(f"`{data}` was processed")
    print('--')


def main():
    template_function(get_text, to_save=True)
    #Got `plain-text`
    #Skip conversion
    #[SAVE]
    #`plain-text` was processed
    template_function(get_pdf, converter=convert_to_text, to_save=True)
    #Got `pdf`
    #[CONVERT]
    #`pdf as text` was processed
    template_function(get_csv, to_save=True)
    #Got `csv`
    #Skip conversion
    #[SAVE]
    #`csv` was processed

if __name__ == "__main__":
    main()