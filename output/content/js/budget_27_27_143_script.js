
  (function() {
    var fn = function() {
      Bokeh.safely(function() {
        (function(root) {
          function embed_document(root) {
            
          var docs_json = '{"aeafcceb-7807-4c84-9abe-f07176ae0753":{"roots":{"references":[{"attributes":{"default_sort":"descending","editor":{"id":"4033","type":"StringEditor"},"field":"fANOVA","formatter":{"id":"4034","type":"StringFormatter"},"title":"fANOVA","width":100},"id":"4027","type":"TableColumn"},{"attributes":{},"id":"4036","type":"StringFormatter"},{"attributes":{"callback":null,"data":{"LPI":["73.46 +/- 0.00","14.02 +/- 0.00","05.50 +/- 0.00","00.00 +/- 0.00"],"Parameters":["lambda_l2","num_leaves","lambda_l1","bagging_freq"],"fANOVA":["67.25 +/- 32.14","00.17 +/- 0.30","08.04 +/- 13.00","08.79 +/- 23.43"]},"selected":{"id":"4037","type":"Selection"},"selection_policy":{"id":"4038","type":"UnionRenderers"}},"id":"4025","type":"ColumnDataSource"},{"attributes":{},"id":"4037","type":"Selection"},{"attributes":{},"id":"4032","type":"StringFormatter"},{"attributes":{},"id":"4035","type":"StringEditor"},{"attributes":{"source":{"id":"4025","type":"ColumnDataSource"}},"id":"4030","type":"CDSView"},{"attributes":{},"id":"4034","type":"StringFormatter"},{"attributes":{},"id":"4038","type":"UnionRenderers"},{"attributes":{"default_sort":"descending","editor":{"id":"4031","type":"StringEditor"},"field":"Parameters","formatter":{"id":"4032","type":"StringFormatter"},"sortable":false,"title":"Parameters","width":150},"id":"4026","type":"TableColumn"},{"attributes":{"columns":[{"id":"4026","type":"TableColumn"},{"id":"4027","type":"TableColumn"},{"id":"4028","type":"TableColumn"}],"height":140,"index_position":null,"source":{"id":"4025","type":"ColumnDataSource"},"view":{"id":"4030","type":"CDSView"}},"id":"4029","type":"DataTable"},{"attributes":{},"id":"4033","type":"StringEditor"},{"attributes":{"default_sort":"descending","editor":{"id":"4035","type":"StringEditor"},"field":"LPI","formatter":{"id":"4036","type":"StringFormatter"},"title":"LPI","width":100},"id":"4028","type":"TableColumn"},{"attributes":{},"id":"4031","type":"StringEditor"}],"root_ids":["4029"]},"title":"Bokeh Application","version":"1.0.1"}}';
          var render_items = [{"docid":"aeafcceb-7807-4c84-9abe-f07176ae0753","roots":{"4029":"df7c95de-a457-42a2-961a-db86b1cac485"}}];
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
