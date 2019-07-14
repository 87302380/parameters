
  (function() {
    var fn = function() {
      Bokeh.safely(function() {
        (function(root) {
          function embed_document(root) {
            
          var docs_json = '{"8db4f7e8-5fa5-4322-82c8-163cf951e444":{"roots":{"references":[{"attributes":{},"id":"4109","type":"StringEditor"},{"attributes":{"source":{"id":"4101","type":"ColumnDataSource"}},"id":"4106","type":"CDSView"},{"attributes":{},"id":"4111","type":"StringEditor"},{"attributes":{},"id":"4107","type":"StringEditor"},{"attributes":{"callback":null,"data":{"LPI":["76.32 +/- 0.00","06.60 +/- 0.00","00.00 +/- 0.00","00.00 +/- 0.00","17.08 +/- 0.00","00.00 +/- 0.00","00.00 +/- 0.00"],"Parameters":["min_data_in_leaf","min_gain_to_split","lambda_l2","feature_fraction","bagging_freq","max_depth","num_leaves"],"fANOVA":["00.00 +/- 0.00","36.79 +/- 47.56","25.00 +/- 43.30","22.95 +/- 40.38","00.44 +/- 1.71","06.25 +/- 24.21","06.25 +/- 24.21"]},"selected":{"id":"4113","type":"Selection"},"selection_policy":{"id":"4114","type":"UnionRenderers"}},"id":"4101","type":"ColumnDataSource"},{"attributes":{"default_sort":"descending","editor":{"id":"4107","type":"StringEditor"},"field":"Parameters","formatter":{"id":"4108","type":"StringFormatter"},"sortable":false,"title":"Parameters","width":150},"id":"4102","type":"TableColumn"},{"attributes":{},"id":"4110","type":"StringFormatter"},{"attributes":{"default_sort":"descending","editor":{"id":"4109","type":"StringEditor"},"field":"fANOVA","formatter":{"id":"4110","type":"StringFormatter"},"title":"fANOVA","width":100},"id":"4103","type":"TableColumn"},{"attributes":{"columns":[{"id":"4102","type":"TableColumn"},{"id":"4103","type":"TableColumn"},{"id":"4104","type":"TableColumn"}],"height":230,"index_position":null,"source":{"id":"4101","type":"ColumnDataSource"},"view":{"id":"4106","type":"CDSView"}},"id":"4105","type":"DataTable"},{"attributes":{},"id":"4108","type":"StringFormatter"},{"attributes":{"default_sort":"descending","editor":{"id":"4111","type":"StringEditor"},"field":"LPI","formatter":{"id":"4112","type":"StringFormatter"},"title":"LPI","width":100},"id":"4104","type":"TableColumn"},{"attributes":{},"id":"4114","type":"UnionRenderers"},{"attributes":{},"id":"4112","type":"StringFormatter"},{"attributes":{},"id":"4113","type":"Selection"}],"root_ids":["4105"]},"title":"Bokeh Application","version":"1.0.1"}}';
          var render_items = [{"docid":"8db4f7e8-5fa5-4322-82c8-163cf951e444","roots":{"4105":"f3889cd9-72f7-4e18-9753-fa43ef14c339"}}];
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
