function weibullCDF(t, t0, T, b)
{
    if (t < t0)
        return 0;

    return 1 - Math.exp(
        -Math.pow(
            (t - t0) / (T - t0),
            b
        )
    );
}

function updatePlot()
{
    let t0 = Number(document.getElementById("t0").value);
    let b = Number(document.getElementById("b").value);
    let T = Number(document.getElementById("T").value);

    document.getElementById("t0Value").innerText = t0;
    document.getElementById("bValue").innerText = b;
    document.getElementById("TValue").innerText = T;

    let x = [];
    let y = [];

    for(let t=0; t<=80000; t+=50)
    {
        x.push(t);
        y.push(
            weibullCDF(t,t0,T,b)
        );
    }

    let data =
    [
        {
            x:x,
            y:y,
            mode:"lines",
            line:{width:3}
        }
    ];

    let layout =
    {
        title:
            `Weibull CDF   t0=${t0}  b=${b}  T=${T}`,

        xaxis:
        {
            title:"Flight Hours"
        },

        yaxis:
        {
            title:"Failure Probability",
            range:[0,1]
        }
    };

    Plotly.newPlot(
        "plot",
        data,
        layout
    );
}

document.getElementById("t0")
    .addEventListener("input", updatePlot);

document.getElementById("b")
    .addEventListener("input", updatePlot);

document.getElementById("T")
    .addEventListener("input", updatePlot);

updatePlot();