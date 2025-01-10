from .._api import _api, Processor

class MessagePop:
    
    @staticmethod
    def show_all_messages():
        '''All messages displayed.'''
        return "/UIS,MSGPOP,0"

    @staticmethod
    def notes_warnings_errors_only():
        '''Only notes, warnings, and errors displayed.'''
        return "/UIS,MSGPOP,1"

    @staticmethod
    def warnings_errors_only():
        '''Only warnings and errors displayed.'''
        return "/UIS,MSGPOP,2"
    
    @staticmethod
    def errors_only():
        '''Only errors displayed.'''
        return "/UIS,MSGPOP,3"


class UIS(_api):

    processor = Processor.any
    msgpop = MessagePop

    @classmethod
    def _check(cls, command):
        raise NotImplementedError
    
    @classmethod
    def call(cls, *args) -> str:
        return f"/{cls.__name__},{','.join(args)}"

    @staticmethod
    def mouse_functionality(left, mid, right):
        '''Controls the functionality of the mouse buttons for dynamic viewing mode only.
        
        1 - PAN, controls dynamic translations.

        2 - ZOOM, controls zoom, and dynamic rotation about the view vector.

        3 - ROTATE, controls dynamic rotation about the screen X and Y axes.

        '''
        return f"/UIS,BORD,{left},{mid},{right}"

    @staticmethod
    def mouse_functionality_reset():
        '''Resets the mouse functionality to the default settings.
        
        default is LEFT = PAN, MIDDLE = ZOOM and RIGHT = ROTATE
        '''
        return "/UIS,BORD"
    
    @staticmethod
    def auto_replot(flag: bool = True):
        '''Controls whether or not an automatic replot occurs after functions affecting the model are executed.
        
        flag:
            True: Auto replot is performed (default).
            False: No auto replot.
        '''
        return f"/UIS,REPLOT,{1 if flag else 0}"
    
    @staticmethod
    def abort(flag: bool = True):
        '''Controls whether or not ANSYS displays dialog boxes to show the status of an operation in progress and to cancel that operation.
        
        flag:
            True: Display status and cancellation dialog boxes.
            False: Do not display status and cancellation dialog boxes.
        '''
        return f"/UIS,ABORT,{1 if flag else 0}"
    
    @staticmethod
    def dynamic_mode_preview(type: int):
        '''Controls whether the dynamic mode preview is a bounding box or the edge outline of the model. This label only applies to 2-D display devices(i.e., /SHOW,XII or /SHOW,WIN32). This "model edge outline" mode is only supported in PowerGraphics [/GRAPHICS,POWER] and is intended for element, line, results, area, or volume displays.
        
        0 - Use model edge outline when possible (default).
        
        1 - Use bounding box preview.
        '''
        return f"/UIS,DYNA,{type}"

    @staticmethod
    def entity_highlighting_by_pick(flag: int):
        '''Controls how graphical entities are highlighted from within the ANSYS Select menu.
        
        0 - Picked keypoints and nodes are enclosed by a square. Picked lines are overlaid by a thicker line. Picked areas, volumes, and elements (non-point/non-line) are redrawn with highlighting colors. However, if the pick is a box, circle, or polygon pick, the highlighting for all entitles consists only of a square placed around the entity's centroid.

        1 - Picked entities are not highlighted.

        2 - 5.1 highlighting (that is, no XOR).

        3 - Picked entities are highlighted as in VALUE = 0, except that, for a box, circle, or polygon pick, the picked areas, volumes, and elements (non-point/non-line) are redrawn with highlighting colors. This technique is slower than the VALUE = 0 technique.

        '''
        return f"/UIS,PICK,{flag}"

    @staticmethod
    def active_power_graphics_when_gui_initiated(flag: bool):
        '''Controls whether or not PowerGraphics is active when the GUI is initiated. The ANSYS program default status is PowerGraphics “ON”; this command is used (placed in the start.ans file) when full graphics is desired on start up.
        
        0 - Start GUI in Full Graphics mode.

        1 - Start GUI in PowerGraphics mode (default).
        '''
        return f"/UIS,POWER,{1 if flag else 0}"

    @staticmethod
    def displays_dynamic_prompt(flag: bool):
        '''Controls whether or not the ANSYS input window displays a dynamic prompt. The dynamic prompt shows the correct command syntax for the command, as you are entering it.
        
        0 - Do not display the dynamic prompt.

        1 - Display the dynamic prompt (default).
        '''
        return f"/UIS,DPRO,{1 if flag else 0}"

    @staticmethod
    def session_editor_include_nonessential(type: int):
        '''Controls whether or not the session editor includes nonessential commands or comments in the file it creates. You can use this option to include comments and other materials in the session editor file.
        
        0 - Do not suppress any commands (default).

        1 - Write the nonessential commands to the session editor file as comments (with a ! at the beginning).

        2 - Do not write nonessential commands or comments.
        '''
        return f"/UIS,UNDO,{type}"

    @staticmethod
    def multi_legend(flag: bool):
        '''Controls whether or not the multi-legend is activated when you start the GUI. The multi-legend enables you to specify the location of your legend items in each of the five graphics windows. You can place this option in your start.ans file and have the GUI start with the legend items in a pre-specified location.
        
        0 - Start GUI with the enhanced legend off (default).

        1 - Start GUI with the enhanced legend capability activated.
        '''
        return f"/UIS,LEGE,{1 if flag else 0}"

    @staticmethod
    def background_shading(flag: bool):
        '''Controls whether or not the background shading is activated when you start the GUI. You can place this option in your start.ans file.
        
        0 - Start the GUI with the no background shading (default).

        1 - Start the GUI with background shading activated.
        '''
        return f"/UIS,PBAK,{1 if flag else 0}"

    @staticmethod
    def windows_prioritization(flag: bool):
        '''Controls the prioritization of your GUI windows when the contents are ported to a plot or print file (/UI,COPY,SAVE). OpenGL (3D) graphics devices require that the ANSYS Graphics Screen contents be set in front of all overlying windows in order to port them to a printer or a file. This operation can sometimes conflict with /NOERASE settings. See the VALUE term (below) to determine the available control options.
        
        0 - No rewrite operations are performed to compensate for items that obscure or overlay the graphics window (default).

        1 - The Graphics screen contents are replotted to ensure that they are situated in front of all other windows. If /NOERASE is detected, this operation is suppressed.
        '''
        return f"/UIS,HPOP,{1 if flag else 0}"
