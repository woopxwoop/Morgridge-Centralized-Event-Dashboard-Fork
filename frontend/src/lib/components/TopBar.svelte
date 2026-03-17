<script lang="ts">
	import { resolve } from '$app/paths';
	import type { EventInfo } from '$lib/mockEvents';
	import SearchBar from '$lib/components/SearchBar.svelte';
	import { formatPeriodLabel } from '$lib/features/calendar/view';
	import {
		calendarReferenceDate,
		calendarStepMode,
		shiftCalendarReferenceDate
	} from '$lib/stores/calendar-ui';

	let { events = [] }: { events: EventInfo[] } = $props();

	const periodLabel = $derived(formatPeriodLabel($calendarReferenceDate, $calendarStepMode));

	function goPrevious(): void {
		calendarReferenceDate.update((currentDate) =>
			shiftCalendarReferenceDate(currentDate, $calendarStepMode, -1)
		);
	}

	function goNext(): void {
		calendarReferenceDate.update((currentDate) =>
			shiftCalendarReferenceDate(currentDate, $calendarStepMode, 1)
		);
	}

	function toggleStepMode(): void {
		if ($calendarStepMode === 'month') {
			calendarStepMode.set('week');
			return;
		}

		if ($calendarStepMode === 'week') {
			calendarStepMode.set('day');
			return;
		}

		calendarStepMode.set('month');
	}

	function goToMonthlyView(): void {
		calendarStepMode.set('month');
	}
</script>

<header class="red-white h-full w-full border-b px-4 py-4">
	<div
		class="mx-auto flex h-full max-w-7xl flex-col gap-3 md:flex-row md:items-center md:justify-between"
	>
		<div class="order-1 w-full md:order-2 md:w-auto md:max-w-sm md:flex-1">
			<SearchBar {events} />
		</div>

		<div class="order-2 flex flex-wrap items-center gap-2 md:order-1">
			<a class="rounded px-3 py-1 text-sm font-bold" href={resolve('/')} onclick={goToMonthlyView}
				>CDIS Calendar</a
			>
			<button
				type="button"
				class="rounded border px-3 py-0.5"
				onclick={goPrevious}
				aria-label="Previous period">&larr;</button
			>
			<p class="min-w-20 text-center text-sm font-semibold sm:min-w-24">{periodLabel}</p>
			<button
				type="button"
				class="rounded border px-3 py-0.5"
				onclick={goNext}
				aria-label="Next period">&rarr;</button
			>
			<button
				type="button"
				class="rounded border px-2 py-1 text-sm"
				onclick={toggleStepMode}
				aria-label="Toggle calendar view mode"
			>
				{#if $calendarStepMode === 'month'}Month
				{:else if $calendarStepMode === 'week'}Week
				{:else}Day{/if}
			</button>
		</div>
	</div>
</header>
