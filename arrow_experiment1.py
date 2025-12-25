import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import QPointF
import math

class ArrowWidget(QWidget):
    def __init__(self, start: QPointF, end: QPointF, parent=None):
        super().__init__(parent)
        self.start = start
        self.end = end
        # Arrowhead parameters

    def paintEvent(self, event):
        arrowhead_length = 20.0
        arrowhead_angle = 25.0
        painter = QPainter(self)
        pen = QPen(QColor("#FF0000"), 2)  # Black pen, width 2
        painter.setPen(pen)

        # Draw the shaft (main line)
        painter.drawLine(self.start, self.end)

        # Calculate arrowhead points
        # Vector from start to end
        dx = self.end.x() - self.start.x()
        dy = self.end.y() - self.start.y()
        length = math.sqrt(dx**2 + dy**2)

        if length == 0:
            return  # No arrow if start and end are the same

        # Unit vector in the direction of the line
        ux = dx / length
        uy = dy / length

        # Rotate unit vector by arrowhead_angle degrees for left side
        angle_rad = math.radians(arrowhead_angle)
        cos_angle = math.cos(angle_rad)
        sin_angle = math.sin(angle_rad)
        # Perpendicular for right side (counter-clockwise rotation)
        left_x = ux * cos_angle - uy * sin_angle
        left_y = ux * sin_angle + uy * cos_angle
        # Perpendicular for left side (clockwise rotation)
        right_x = ux * cos_angle + uy * sin_angle
        right_y = -ux * sin_angle + uy * cos_angle

        # Arrowhead tip is at end
        # Left point: move backward along left direction subtracted from a reduced end
        arrowhead_left = QPointF(
            self.end.x() - arrowhead_length * left_x,
            self.end.y() - arrowhead_length * left_y
        )
        arrowhead_right = QPointF(
            self.end.x() - arrowhead_length * right_x,
            self.end.y() - arrowhead_length * right_y
        )

        # Draw the arrowhead lines
        painter.drawLine(self.end, arrowhead_left)
        painter.drawLine(self.end, arrowhead_right)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ArrowWidget(QPointF(200, 150), QPointF(50, 50))
    widget.setGeometry(100, 100, 400, 300)  # Adjust size as needed
    widget.show()
    sys.exit(app.exec())
