
  (function() {
    var fn = function() {
      Bokeh.safely(function() {
        (function(root) {
          function embed_document(root) {
            
          var docs_json = '{"7cc4487f-3bbe-4074-bdf1-10e79ecd5d3b":{"roots":{"references":[{"attributes":{},"id":"4072","type":"StringFormatter"},{"attributes":{"default_sort":"descending","editor":{"id":"4073","type":"StringEditor"},"field":"LPI","formatter":{"id":"4074","type":"StringFormatter"},"title":"LPI","width":100},"id":"4066","type":"TableColumn"},{"attributes":{"default_sort":"descending","editor":{"id":"4071","type":"StringEditor"},"field":"fANOVA","formatter":{"id":"4072","type":"StringFormatter"},"title":"fANOVA","width":100},"id":"4065","type":"TableColumn"},{"attributes":{},"id":"4071","type":"StringEditor"},{"attributes":{"callback":null,"data":{"LPI":["36.69 +/- 0.00","47.47 +/- 0.00","08.56 +/- 0.00","05.86 +/- 0.00"],"Parameters":["bagging_fraction","bagging_freq","lambda_l2","num_leaves"],"fANOVA":["48.63 +/- 43.80","10.74 +/- 24.54","25.27 +/- 36.76","00.34 +/- 0.72"]},"selected":{"id":"4075","type":"Selection"},"selection_policy":{"id":"4076","type":"UnionRenderers"}},"id":"4063","type":"ColumnDataSource"},{"attributes":{},"id":"4070","type":"StringFormatter"},{"attributes":{"columns":[{"id":"4064","type":"TableColumn"},{"id":"4065","type":"TableColumn"},{"id":"4066","type":"TableColumn"}],"height":140,"index_position":null,"source":{"id":"4063","type":"ColumnDataSource"},"view":{"id":"4068","type":"CDSView"}},"id":"4067","type":"DataTable"},{"attributes":{"default_sort":"descending","editor":{"id":"4069","type":"StringEditor"},"field":"Parameters","formatter":{"id":"4070","type":"StringFormatter"},"sortable":false,"title":"Parameters","width":150},"id":"4064","type":"TableColumn"},{"attributes":{},"id":"4069","type":"StringEditor"},{"attributes":{},"id":"4073","type":"StringEditor"},{"attributes":{},"id":"4075","type":"Selection"},{"attributes":{"source":{"id":"4063","type":"ColumnDataSource"}},"id":"4068","type":"CDSView"},{"attributes":{},"id":"4074","type":"StringFormatter"},{"attributes":{},"id":"4076","type":"UnionRenderers"}],"root_ids":["4067"]},"title":"Bokeh Application","version":"1.0.1"}}';
          var render_items = [{"docid":"7cc4487f-3bbe-4074-bdf1-10e79ecd5d3b","roots":{"4067":"ce578168-3939-4847-a178-90f9582fcae6"}}];
          root.Bokeh.embed.embed_items(docs_json, render_items);
        
          }
          if (root.Bokeh !== undefined) {
            embed_document(root);
          } else {
            var attempts = 0;
            var timer = setInterval(function(root) {
              if (root.Bokeh !== undefined) {
                embed_document(root);
                clearInterval(timer);
              }
              attempts++;
              if (attempts > 100) {
                console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                clearInterval(timer);
              }
            }, 10, root)
          }
        })(window);
      });
    };
    if (document.readyState != "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  })();
