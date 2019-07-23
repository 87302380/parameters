
  (function() {
    var fn = function() {
      Bokeh.safely(function() {
        (function(root) {
          function embed_document(root) {
            
          var docs_json = '{"267041bb-2326-4bdf-a226-aceee5e1e4ae":{"roots":{"references":[{"attributes":{"source":{"id":"3987","type":"ColumnDataSource"}},"id":"3992","type":"CDSView"},{"attributes":{},"id":"3994","type":"StringFormatter"},{"attributes":{"callback":null,"data":{"LPI":["81.48 +/- 0.12","17.66 +/- 0.05","00.00 +/- 0.00","00.38 +/- 0.00"],"Parameters":["feature_fraction","bagging_fraction","bagging_freq","lambda_l2"],"fANOVA":["46.99 +/- 37.62","17.23 +/- 28.83","12.08 +/- 25.16","08.92 +/- 24.95"]},"selected":{"id":"3999","type":"Selection"},"selection_policy":{"id":"4000","type":"UnionRenderers"}},"id":"3987","type":"ColumnDataSource"},{"attributes":{"default_sort":"descending","editor":{"id":"3995","type":"StringEditor"},"field":"fANOVA","formatter":{"id":"3996","type":"StringFormatter"},"title":"fANOVA","width":100},"id":"3989","type":"TableColumn"},{"attributes":{"columns":[{"id":"3988","type":"TableColumn"},{"id":"3989","type":"TableColumn"},{"id":"3990","type":"TableColumn"}],"height":140,"index_position":null,"source":{"id":"3987","type":"ColumnDataSource"},"view":{"id":"3992","type":"CDSView"}},"id":"3991","type":"DataTable"},{"attributes":{"default_sort":"descending","editor":{"id":"3997","type":"StringEditor"},"field":"LPI","formatter":{"id":"3998","type":"StringFormatter"},"title":"LPI","width":100},"id":"3990","type":"TableColumn"},{"attributes":{},"id":"3993","type":"StringEditor"},{"attributes":{},"id":"3996","type":"StringFormatter"},{"attributes":{},"id":"3998","type":"StringFormatter"},{"attributes":{},"id":"4000","type":"UnionRenderers"},{"attributes":{},"id":"3997","type":"StringEditor"},{"attributes":{},"id":"3995","type":"StringEditor"},{"attributes":{},"id":"3999","type":"Selection"},{"attributes":{"default_sort":"descending","editor":{"id":"3993","type":"StringEditor"},"field":"Parameters","formatter":{"id":"3994","type":"StringFormatter"},"sortable":false,"title":"Parameters","width":150},"id":"3988","type":"TableColumn"}],"root_ids":["3991"]},"title":"Bokeh Application","version":"1.0.1"}}';
          var render_items = [{"docid":"267041bb-2326-4bdf-a226-aceee5e1e4ae","roots":{"3991":"5acf3d1c-359e-4a7f-8840-58fed2bb3a13"}}];
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
