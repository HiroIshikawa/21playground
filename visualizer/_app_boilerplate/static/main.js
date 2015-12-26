// custom javascript
$(function() {
  console.log('jquery is working!');
  createGraph();
});

function createGraph() {
  // Code goes here
	var width = 960; // chart width
	var height = 700; // chart height
	var format = d3.format(",d");  // convert value to integer
	var color = d3.scale.category20();  // create ordinal scale with 20 colors
	var sizeOfRadius = d3.scale.pow().domain([-100,100]).range([-50,50]);  // https://github.com/mbostock/d3/wiki/Quantitative-Scales#pow
	var bubble = d3.layout.pack()
	.sort(null)  // disable sorting, use DOM tree traversal
	.size([width, height])  // chart layout size
	.padding(1)  // padding between circles
	.radius(function(d) { return 20 + (sizeOfRadius(d) * 30); });  // radius for each circle

}