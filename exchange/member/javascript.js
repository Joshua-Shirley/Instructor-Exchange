class Resort {
    constructor(name, location) {
        this.name = name;
        this.location = location;
    }
}

function downloadFile(content, filename, mimeType) {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  URL.revokeObjectURL(url);
  document.body.removeChild(link);
}

function resort_list() {    
    var theList = {
        "vail" : []
    }
    
    var rows = document.querySelectorAll("#mw-content-text > div.mw-content-ltr.mw-parser-output > table.wikitable.sortable.jquery-tablesorter > tbody tr");

    rows.forEach(row => {
        var columns = row.querySelectorAll("td");
        var area = columns[0].innerText;
        var location = columns[1].querySelectorAll("a")[1].innerText;        
        var resort = new Resort(area, location);
        console.log(resort);
        theList["vail"].push(resort);
    });
    
    return JSON.stringify(theList);
}

var resort_list = resort_list();
downloadFile( resort_list , "vail-resorts", "text/plain");

