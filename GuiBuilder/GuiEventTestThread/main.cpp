#include "mainwindow.h"
#include <QApplication>
#include "threadgui.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    ThreadGui tg;
    w.show();
    tg.show();

    return a.exec();
}
