#ifndef THREADGUI_H
#define THREADGUI_H

#include <QWidget>

namespace Ui {
class ThreadGui;
}

class ThreadGui : public QWidget
{
    Q_OBJECT

public:
    explicit ThreadGui(QWidget *parent = 0);
    ~ThreadGui();

private:
    Ui::ThreadGui *ui;
};

#endif // THREADGUI_H
