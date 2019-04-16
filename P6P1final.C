//Example of reading data file and plotting
#include <iostream> 
#include <TGraph.h>

void P6P1final(){
    TGraph *g = new TGraph("~/Git-Repositories/22-061-Psets/REBCOExperiment_IVData.dat", "%lg %lg", "\t,");
    //g->SetMarkerType(21);


    //Define Fit Function
    TF1 *f = new TF1("f", "20*(x/[0])^[1]", 0,5); 
    f->SetParNames("Initial", "Secondary", "Tertiary", "Quartinary");
    f->SetParameters(100 , 20);
    //TF1 *f = new TF1("f", "[0]*e^([1]*x)+[2]", 0,5);
    g->Fit(f);

    //Draw the Function
    g->SetLineColor(kBlack);
    g->SetTitle("REBCO-Experiment IV Data;Current [A];Voltage [uV]");
    g->Draw("ALP");
}
