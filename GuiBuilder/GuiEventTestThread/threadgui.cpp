#include "threadgui.h"
#include "ui_threadgui.h"

ThreadGui::ThreadGui(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::ThreadGui)
{
    ui->setupUi(this);
}

ThreadGui::~ThreadGui()
{
    delete ui;
}
