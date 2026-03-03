<script lang="ts">
	import {
		calendarReferenceDate,
		calendarSearchQuery,
		calendarStepMode,
		shiftCalendarReferenceDate,
		type CalendarStepMode
	} from '$lib/stores/calendar-ui';

	function formatPeriodLabel(date: Date, mode: CalendarStepMode): string {
		if (mode === 'month') {
			return new Intl.DateTimeFormat('en-US', { month: 'long', year: 'numeric' }).format(date);
		}

		if (mode === 'day') {
			return new Intl.DateTimeFormat('en-US', {
				weekday: 'short',
				month: 'short',
				day: 'numeric',
				year: 'numeric'
			}).format(date);
		}

		const weekStart = new Date(date);
		weekStart.setDate(weekStart.getDate() - weekStart.getDay());
		const weekEnd = new Date(weekStart);
		weekEnd.setDate(weekStart.getDate() + 6);

		const shortFormatter = new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric' });
		return `${shortFormatter.format(weekStart)} - ${shortFormatter.format(weekEnd)}`;
	}

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
</script>

<header class="red-white w-full border-b px-4 py-4">
	<div class="mx-auto flex max-w-7xl flex-wrap items-center justify-between gap-3">
		<div class="flex items-center gap-2">
			<a class="rounded px-3 py-1 text-sm font-bold" href="/">Title?</a>
			<button
				type="button"
				class="rounded border px-3 py-0.5"
				onclick={goPrevious}
				aria-label="Previous period">&larr;</button
			>
			<p class="min-w-24 text-center text-sm font-semibold">{periodLabel}</p>
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

		<label class="w-full max-w-sm flex-1">
			<span class="sr-only">Search events</span>
			<input
				type="search"
				placeholder="Search events"
				class="w-full rounded border px-3 py-1.5 text-sm"
				bind:value={$calendarSearchQuery}
			/>
		</label>
	</div>
</header>
