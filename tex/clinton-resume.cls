%----------------------------------------------------------------------------------------
%	CLASS OPTIONS AND REQUIRED PACKAGES
%----------------------------------------------------------------------------------------

\ProvidesClass{clinton-resume}[2014/04/30 CV class]
\NeedsTeXFormat{LaTeX2e}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass{article}
%----------PACKAGES--------
\usepackage[hmargin=1.25cm, vmargin=0.75cm]{geometry} % Specifies horizontal and vertical page margins
\usepackage{hyperref} % Required for links
\usepackage{fontawesome}
\usepackage{tikz}
\usepackage{mdframed}
%\usepackage[usenames,dvipsnames]{xcolor}
%\@ifpackageloaded{tex4ht}{

%}{
\newcommand{\lastupdated}{ % Create a new command for printing the Last Updated text
\begin{textblock}{25}(75,2) % The position of the Last Updated text on the page (75% of the page across, 2% down)
\color{date}\fontspec[Path = ../otf/]{Raleway-ExtraLight}\fontsize{8pt}{10pt}\selectfont % Text styling of the text
Last Updated on \today % Last Updated text
\end{textblock}}

 \usepackage{fontspec}
%----------NEW COMMANDS--------
%	FONTS
%----------------------------------------------------------------------------------------

 % Required for specifying custom fonts in XeLaTeX

\setmainfont[Color=primaryText, Path = ../ttf/,BoldItalicFont=Lato-RegIta,BoldFont=Lato-Reg,ItalicFont=Lato-LigIta]{Lato-Lig} % The primary font for content text; defines bold, italic and bold-italic as well

\setsansfont[Scale=MatchLowercase,Mapping=tex-text, Path = ../otf/]{Raleway-ExtraLight} % The font used where \sfffamily is called
  
%----------------------------------------------------------------------------------------
%	SECTION TITLE STYLING AND SPACING
%----------------------------------------------------------------------------------------

\usepackage{titlesec} % Required for customizing section/subsection/etc titles

\titlespacing{\section}{0pt}{0pt}{0pt} % Removes the spacing around the main section titles
\titlespacing{\subsection}{0pt}{0pt}{0pt} % Removes the spacing around the subsections
\newcommand{\sectionspace}{\vspace{8pt}} % Defines a command to add a set amount of space after sections and subsections

\titleformat{\section}{ % Customize the large section titles
\color{headings}\scshape\fontspec[Path = ../ttf/]{Lato-Lig}\fontsize{16pt}{24pt}\selectfont \raggedright\uppercase}{}{0em}{}

\titleformat{\subsection}{ % Customize the subsections and places worked/studied titles
\color{subheadings}\fontspec[Path = ../ttf/]{Lato-Bol}\fontsize{12pt}{12pt}\selectfont\bfseries\uppercase}{}{0em}{}

\newcommand{\runsubsection}[1]{ % Used for creating subsections where a description is required on the same line
\color{subheadings}\fontspec[Path = ../ttf/]{Lato-Bol}\fontsize{12pt}{12pt}\selectfont\bfseries\uppercase {#1} \normalfont}

\newcommand{\descript}[1]{ % Used for describing the subsection either on the same line or underneath
\color{subheadings}\raggedright\scshape\fontspec[Path = ../otf/]{Raleway-Medium}\fontsize{11pt}{13pt}\selectfont {#1 \\} \normalfont}

\newcommand{\location}[1]{ % Used for specifying a duration and/or location under a subsection
\color{subheadings}\raggedright\fontspec[Path = ../otf/]{Raleway-Medium}\fontsize{10pt}{12pt}\selectfont {#1\\} \normalfont}

%----------------------------------------------------------------------------------------
%	MAIN HEADING COMMAND
%----------------------------------------------------------------------------------------

\newcommand{\namesection}[3]{ % Defines the command for the main heading
\centering{ % Center the name
\fontsize{30pt}{40pt} % Font size
\fontspec[Path = ../ttf/]{Lato-Lig}\selectfont #1 % First name font
\fontspec[Path = ../ttf/]{Lato-Lig}\selectfont #2 % Last name font
} \\[5pt] % Whitespace between the name and contact information
\centering{ % Center the contact information
\color{headings} % Use the headings color
\fontspec[Path = ../otf/]{Raleway-Medium}\fontsize{11pt}{14pt}\selectfont #3} % Contact information font
\noindent\makebox[\linewidth]{\color{headings}\rule{\paperwidth}{0.4pt}} % Horizontal rule
\vspace{-5pt} % Reduce whitespace after the rule slightly
}

%}%end of \@ifpackageloaded{tex4ht}{


\usepackage[absolute]{textpos} % Required for positioning the Last Updated text at the top right of the page
\usepackage[UKenglish]{isodate} % Prints the Last Updated date in UK English format
%----------PACKAGES--------

%----------NEW COMMANDS--------
\newcommand*\circled[1]{\tikz[baseline=(char.base)]{
            \node[shape=circle,draw,inner sep=2pt,red] (char) {#1};}}
%----------NEW COMMANDS--------

%----------GS SNAKE COLOR PALETTE--------http://www.color-hex.com/color-palette/5274
\definecolor{primaryText}{HTML}{000000}
\definecolor{sectionText}{HTML}{2E4242}
\definecolor{subsectionText}{HTML}{6C8392}
\definecolor{subsubsectionText}{HTML}{ADC4CE}
\definecolor{itemizedBoxColor}{HTML}{FDFDFF}
\definecolor{itemizedBoxLineColor}{HTML}{EEEEEE}
%----------GS SNAKE COLOR PALETTE--------http://www.color-hex.com/color-palette/5274
%----------OTHER COLORS----------
\definecolor{primary}{HTML}{2b2b2b} % The primary document color for content text
\definecolor{headings}{HTML}{6A6A6A} % The color of the large sections
\definecolor{subheadings}{HTML}{333333} % The color of subsections and places worked/studied
\definecolor{date}{HTML}{666666} % The color used for the Last Updated text at the top right
%----------OTHER COLORS----------

%----------NEW ENVIRONMENTS--------
\newmdenv[backgroundcolor=itemizedBoxColor,
          roundcorner=40pt,
          linecolor=itemizedBoxLineColor,
          ]{myframedenv}

%----------NEW ENVIRONMENTS--------
%----------NEW COMMANDS--------
\renewcommand*\circled[1]{
	\tikz[baseline=(char.base)]{
            \node[shape=circle,
            		draw,inner sep=2pt,backgroundcolor=itemizedBoxColor,
            		linecolor=primaryText
            		] (char) {#1};}}


%----------------------------------------------------------------------------------------
%	LAST UPDATED COMMAND
%----------------------------------------------------------------------------------------



\setlength{\TPHorizModule}{0.01\paperwidth} % Sets the units for the horizontal position used in the \begin{textblock} argument
\setlength{\TPVertModule}{0.01\paperwidth} % Sets the units for the vertical position used in the \begin{textblock} argument




%----------------------------------------------------------------------------------------
%	SECTION TITLE STYLING AND SPACING
%----------------------------------------------------------------------------------------

\newenvironment{tightitemize} % Defines the tightitemize environment which modifies the itemize environment to be more compact
{\vspace{-\topsep}
	\begin{myframedenv}
		\begin{itemize}
			\itemsep1pt \parskip0pt \parsep0pt}
		{\end{itemize}
	\end{myframedenv}
\vspace{-\topsep}}

\newenvironment{tighttabular} % Defines the tightitemize environment which modifies the itemize environment to be more compact
{
	\begin{myframedenv}
		\begin{tabular}{l}
		}
		{\end{tabular}
	\end{myframedenv}
\vspace{-\topsep}}

\newenvironment{tightTabularPresentations} % Defines the tightitemize environment which modifies the itemize environment to be more compact
{
	\begin{myframedenv}
		\begin{tabular}{ll}
		}
		{\end{tabular}
	\end{myframedenv}
\vspace{-\topsep}}