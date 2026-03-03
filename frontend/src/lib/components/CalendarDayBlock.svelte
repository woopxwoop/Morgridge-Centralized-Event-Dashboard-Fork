<script lang="ts">
	import { calendarReferenceDate, calendarStepMode } from '$lib/stores/calendar-ui';

	let { dayNumber, date }: { dayNumber: number; date: Date } = $props();

	function toLocalIsoDate(value: Date): string {
		const year = value.getFullYear();
		// month is 0 indexed, but humans use 1-12
		const month = String(value.getMonth() + 1).padStart(2, '0');
		const day = String(value.getDate()).padStart(2, '0');
		return `${year}-${month}-${day}`;
	}

	const dateParam = $derived(toLocalIsoDate(date));

	function openDayView(event: MouseEvent): void {
		event.preventDefault();
		calendarReferenceDate.set(new Date(date));
		calendarStepMode.set('day');
	}
</script>

<div class="flex h-full w-full items-start justify-center">
	<a class="px-1" href={`/day?date=${dateParam}`} onclick={openDayView}>{dayNumber}</a>
</div>
