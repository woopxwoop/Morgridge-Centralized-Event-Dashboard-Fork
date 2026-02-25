<script lang="ts">
	let { dayNumber, date }: { dayNumber: number; date: Date } = $props();

	function toLocalIsoDate(value: Date): string {
		const year = value.getFullYear();
		// month is 0 indexed, but humans use 1-12
		const month = String(value.getMonth() + 1).padStart(2, '0');
		const day = String(value.getDate()).padStart(2, '0');
		return `${year}-${month}-${day}`;
	}

	const dateParam = $derived(toLocalIsoDate(date));
</script>

<div>
	<a href={`/day?date=${dateParam}`}> {dayNumber} </a>
</div>
