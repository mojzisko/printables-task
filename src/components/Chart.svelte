<script>
  export let data = [];

  const size = 500;
  const radius = size / 2; // Radius of the pie chart

  // Predefined colors for each candidate
  const candidateColors = {
    "1": "#4175E0",
    "2": "#C05F2F",
    "4": "#72846B",
    "5": "#81A6BA",
    "6": "#A64D79",
    "7": "#33CCCC",
    "8": "#36DA83",
    "9": "#E5DF7F",
  };

  // Total votes calculation
  const totalVotes = data.reduce(
    (total, { votes }) => total + Number(votes),
    0
  );

  // Slices calculation: transforming vote counts into pie chart slices
  let startAngle = 0;
  const slices = data.map((item) => {
    const value = Number(item.votes);
    const percentage = (value / totalVotes) * 100;
    const angle = (percentage / 100) * 360; // Angle corresponding to the vote percentage
    const endAngle = startAngle + angle; // Determine the end angle of the slice

    const slice = {
      startAngle,
      endAngle,
      color: candidateColors[item.poradoveCislo] || "#999", // Assign color or default
    };
    startAngle = endAngle; // Prepare start angle for the next slice
    return slice;
  });

  // Describe an SVG arc path for each pie chart slice
  function describeArc(x, y, radius, startAngle, endAngle) {
    const start = polarToCartesian(x, y, radius, endAngle);
    const end = polarToCartesian(x, y, radius, startAngle);
    const largeArcFlag = endAngle - startAngle <= 180 ? "0" : "1";
    return [
      "M",
      start.x,
      start.y,
      "A",
      radius,
      radius,
      0,
      largeArcFlag,
      0,
      end.x,
      end.y,
      "L",
      x,
      y,
      "Z",
    ].join(" ");
  }

  // Convert polar coordinates to Cartesian
  function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
    const angleInRadians = ((angleInDegrees - 90) * Math.PI) / 180.0;
    return {
      x: centerX + radius * Math.cos(angleInRadians),
      y: centerY + radius * Math.sin(angleInRadians),
    };
  }
</script>

<svg width={size} height={size} viewBox={`0 0 ${size} ${size}`} class="mx-auto">
  {#each slices as { startAngle, endAngle, color }}
    <path
      d={describeArc(radius, radius, radius - 30, startAngle, endAngle)}
      fill={color}
    />
  {/each}
</svg>

<style>
  svg {
    transform: rotate(-90deg);
  } /* Rotate SVG to start the chart from the top */
</style>
