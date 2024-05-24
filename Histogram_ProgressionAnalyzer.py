from graphics import *

def graph_for_histogram ( progress_height , trailer_height , retriever_height, exclusion_height ) :

    window = GraphWin ('Histogram' , 500 , 500 )

    window.setBackground ( color_rgb( 114 , 137 , 171 ) )

# Caluculating the total height.
    total = progress_height + trailer_height + retriever_height + exclusion_height

 # =============================== Height ================================ #   

# Column data height
    progress_percentage  = 430 - ( 430 * progress_height / total )
    trailer_percentage   = 430 - ( 430 * trailer_height / total )
    retriever_percentage = 430 - ( 430 * retriever_height / total )
    exclusion_percentage = 430 - ( 430 * exclusion_height / total )

# Number of data of the column
    progress_column_data  = 420 - ( 430 * progress_height / total )
    trailer_column_data   = 420 - ( 430 * trailer_height / total )
    retriever_column_data = 420 - ( 430 * retriever_height / total )
    exclusion_column_data = 420 - ( 430 * exclusion_height / total )

# ======================================================================== #


# =============================== Columns ================================ #

# Constructing a RECTANGLE
    progress_column  = Rectangle ( Point(115,430) , Point(15,progress_percentage) )
    trailing_column  = Rectangle ( Point(235,430) , Point(135,trailer_percentage) )
    retriever_column = Rectangle ( Point(355,430) , Point(255,retriever_percentage) )
    exclusion_column = Rectangle ( Point(475,430) , Point(375,exclusion_percentage) )
    
# Displaying the rectangles
    progress_column.draw  (window)
    trailing_column.draw  (window)
    retriever_column.draw (window)
    exclusion_column.draw (window)

# ======================================================================== #

# ============================ Virticle Line ============================= #

# Constructing a virticle line
    virticle_line = Line ( Point(0,430) , Point(500,430) )

# Displaying the virticle line
    virticle_line.draw (window)

# ======================================================================== #

# ============================ Colored Columns =========================== #

    progress_column.setFill  ( color_rgb(127, 230, 127) )
    trailing_column.setFill  ( color_rgb(185, 230, 127) )
    retriever_column.setFill ( color_rgb(192, 224, 192) )
    exclusion_column.setFill ( color_rgb(230, 127, 127) )

# ======================================================================== #

# ============================= Column Texts ============================= #

# Constructing column texts
    progress_text  = Text ( Point(65,445)  , "Progress" )
    trailing_text  = Text ( Point(180,445) , "Trailing" )
    retriever_text = Text ( Point(300,445) , "Retriever" )
    exclusion_text = Text ( Point(420,445) , "Excluded" )

# Implementing the number of data in each column as texts
    progress_values  = Text ( Point(65,progress_column_data)   , f"{progress_height}" )
    trailing_values  = Text ( Point(180,trailer_column_data)   , f"{trailer_height}" )
    retriever_values = Text ( Point(300,retriever_column_data) , f"{retriever_height}"  )
    exclusion_values = Text ( Point(420,exclusion_column_data) , f"{exclusion_height}" )

# Constructing a heading text
    histogram_heading = Text ( Point(120,40) , "Histogram Results" )

# Implementing the total number of outcomes 
    total_outcomes = Text ( Point(200,480) , f"{total} outcomes in total." )

# Adding styles to column texts
    progress_text.setStyle  ("bold") 
    trailing_text.setStyle  ("bold")
    retriever_text.setStyle ("bold")
    exclusion_text.setStyle ("bold")

# Adding colors to column texts
    progress_text.setTextColor  ( color_rgb(67, 67, 61) )
    trailing_text.setTextColor  ( color_rgb(67, 67, 61) )
    retriever_text.setTextColor ( color_rgb(67, 67, 61) )
    exclusion_text.setTextColor ( color_rgb(67, 67, 61) )

# Histogram header style
    histogram_heading.setStyle ("bold")
    histogram_heading.setSize(17)

# Total outcomes text style
    total_outcomes.setStyle ("bold")

# Displaying column texts    
    progress_text.draw  (window)
    trailing_text.draw  (window)
    retriever_text.draw (window)
    exclusion_text.draw (window)

# Displaying number of data in each column
    progress_values.draw  (window)
    trailing_values.draw  (window)
    retriever_values.draw (window)
    exclusion_values.draw (window)

# Displaying histogram header
    histogram_heading.draw (window)

# Displaying the total number of outcomes
    total_outcomes.draw (window)

# ================================================================= #

    window.getMouse()
    window.close ()
