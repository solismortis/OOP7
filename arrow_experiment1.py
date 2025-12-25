import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush
from PyQt6.QtCore import pyqtSignal, QPoint, Qt


# Observer Pattern Interfaces and Base Classes
class Observer:
    def update(self, position: QPoint):
        """Called when the subject changes."""
        pass


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, position: QPoint):
        for observer in self._observers:
            observer.update(position)


# Concrete Subject: The leader circle with movement notifications
class Circle(Subject):
    def __init__(self, position: QPoint, radius: int = 20, color: QColor = QColor("black")):
        super().__init__()
        self.position = position
        self.radius = radius
        self.color = color

    def move_to(self, position: QPoint):
        self.position = position
        self.notify_observers(position)  # Notify observers of the move


# Concrete Observer: The follower circle that react to the leader's movement
class FollowerCircle(Observer, Circle):
    def __init__(self, position: QPoint, radius: int = 20, color: QColor = QColor("red")):
        # Initialize as Observer and also a Circle (for drawing)
        Observer.__init__(self)
        Circle.__init__(self, position, radius, color)
        self.offset = QPoint(50, 50)  # Follow with an offset

    def update(self, leader_position: QPoint):
        # Follow the leader's position with an offset
        self.position = leader_position + self.offset


# Drawing Widget: Displays and handles interaction for the shapes
class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Observer Pattern: Following Circles")
        self.setFixedSize(400, 300)

        # Create leader and follower
        self.leader = Circle(QPoint(100, 100), radius=20, color=QColor("black"))
        self.follower = FollowerCircle(QPoint(150, 150), radius=15, color=QColor("red"))

        # Attach the follower as an observer of the leader
        self.leader.attach(self.follower)

        self.dragging_leader = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor("black"), 2))

        # Draw leader (filled circle)
        painter.setBrush(QBrush(self.leader.color))
        painter.drawEllipse(self.leader.position, self.leader.radius, self.leader.radius)

        # Draw follower (filled circle)
        painter.setBrush(QBrush(self.follower.color))
        painter.drawEllipse(self.follower.position, self.follower.radius, self.follower.radius)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if (event.pos() - self.leader.position).manhattanLength() < self.leader.radius:
                self.dragging_leader = True

    def mouseMoveEvent(self, event):
        if self.dragging_leader:
            self.leader.move_to(event.pos())
            self.update()  # Trigger repaint

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging_leader = False


# Main Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = DrawingWidget()
    widget.show()
    sys.exit(app.exec())
