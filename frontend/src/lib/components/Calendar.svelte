<script lang="ts">
	import CalendarDayBlock from '$lib/components/CalendarDayBlock.svelte';
	import { calendarReferenceDate, calendarStepMode } from '$lib/stores/calendar-ui';

	const displayedYear = $derived($calendarReferenceDate.getFullYear());
	const displayedMonth = $derived($calendarReferenceDate.getMonth());

	const firstDayOfMonth = $derived(new Date(displayedYear, displayedMonth, 1));
	const firstDayOfWeek = $derived(firstDayOfMonth.getDay());
	const firstVisibleDate = $derived(new Date(displayedYear, displayedMonth, 1 - firstDayOfWeek));

	const monthLabel = $derived(
		new Intl.DateTimeFormat('en-US', { month: 'long', year: 'numeric' }).format(
			new Date(displayedYear, displayedMonth, 1)
		)
	);

	const days: string[] = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

	const calendarDays = $derived(
		Array.from({ length: 42 }, (_, index) => {
			const date = new Date(firstVisibleDate);
			date.setDate(firstVisibleDate.getDate() + index);

			return {
				date,
				dayNumber: date.getDate(),
				isCurrentMonth: date.getMonth() === displayedMonth
			};
		})
	);

	const weeks = $derived(
		Array.from({ length: 6 }, (_, weekIndex) =>
			calendarDays.slice(weekIndex * 7, (weekIndex + 1) * 7)
		)
	);

	const currentWeekDays = $derived(
		Array.from({ length: 7 }, (_, index) => {
			const weekStart = new Date($calendarReferenceDate);
			weekStart.setDate(weekStart.getDate() - weekStart.getDay());

			const date = new Date(weekStart);
			date.setDate(weekStart.getDate() + index);

			return {
				date,
				dayNumber: date.getDate(),
				isCurrentMonth: date.getMonth() === displayedMonth
			};
		})
	);
</script>

<div class="h-full w-full">
	<table class="h-full w-full table-fixed border-collapse">
		<thead>
			<tr>
				{#each days as day}
					<th class="pb-4 font-medium">{day}</th>
				{/each}
			</tr>
		</thead>
		{#if $calendarStepMode === 'week'}
			<tbody>
				<tr>
					{#each currentWeekDays as day}
						<td class="p align-top">
							<div class={day.isCurrentMonth ? '' : 'opacity-40'}>
								<CalendarDayBlock date={day.date} dayNumber={day.dayNumber} />
							</div>
						</td>
					{/each}
				</tr>
			</tbody>
		{:else}
			<tbody class="h-full grid-rows-6">
				{#each weeks as week}
					<tr class="row-span-1">
						{#each week as day}
							<td class="p align-top">
								<div class={day.isCurrentMonth ? '' : 'opacity-40'}>
									<CalendarDayBlock date={day.date} dayNumber={day.dayNumber} />
								</div>
							</td>
						{/each}
					</tr>
				{/each}
			</tbody>
		{/if}
	</table>
</div>
