#include <iostream>
#include "TGraph.h"
#include "TCanvas.h"


void P6P1T2(){
    auto c = new TCanvas(); c->SetGrid();
    TGraphErrors("~/Git-Repositories/22-061-Psets/REBCOExperiment_IVData.dat","%lg %lg","\t,");
    graph_expected.SetTitle("REBCO - IV - Experimental Data;" "Current [A];" "Voltage [uV]");
    graph_expected.SetFillColor(kYellow);
    graph_expected.DrawClone("E3AL"); 

    TLegend leg(.1, .7, .3 , .9, "REBCO-Experimental Data")
    leg.SetFillColor(0);
    leg.AddEntry(&graph_expected, "REBCO - Experimental Results")
    /*Include the same as above, but with Fit Line too*/
    leg.DrawClone("Same");

    graph.Print();
}
