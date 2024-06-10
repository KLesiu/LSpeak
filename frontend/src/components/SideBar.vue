<script setup lang="ts">
</script>

<template>
    <aside >
        <div class="menu__tab">
            <svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#clip0_7_63)">
            <path d="M19.9846 12.5452C20.4127 10.7987 20.333 8.96631 19.7549 7.26359C19.1768 5.56087 18.1243 4.05871 16.7214 2.9339C15.3184 1.80909 13.6234 1.10843 11.8357 0.914379C10.048 0.720331 8.24208 1.04097 6.63047 1.83856C5.01885 2.63615 3.66859 3.8775 2.73861 5.41652C1.80862 6.95554 1.33761 8.72819 1.38099 10.5258C1.42438 12.3235 1.98036 14.0714 2.9835 15.5637C3.98665 17.0561 5.39521 18.2309 7.04343 18.9498M1.37772 10.2961H20.2537" stroke="#E60060" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M8.012 14.652C7.53819 13.2446 7.25903 11.7791 7.18229 10.296C7.36074 6.84427 8.6323 3.53868 10.8131 0.857178C12.9934 3.5389 14.2643 6.84446 14.4423 10.296C14.4114 10.9015 14.3467 11.5047 14.2486 12.1029M16.7137 14.0195L23.6223 17.0126L16.7137 20.0057L9.80857 17.0126L16.7171 14.0195H16.7137Z" stroke="#E60060" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M12.9406 18.3771L12.9474 21.6343C12.9474 21.6343 14.0874 23.1429 16.7137 23.1429C19.34 23.1429 20.4851 21.6343 20.4851 21.6343V18.3771M9.80686 22.2771V17.0126" stroke="#E60060" stroke-linecap="round" stroke-linejoin="round"/>
            </g>
            <defs>
            <clipPath id="clip0_7_63">
            <rect width="24" height="24" fill="white" transform="translate(0.5)"/>
            </clipPath>
            </defs>
            </svg>
            <span>Learn</span>
        </div>
    </aside>
</template>

<style scoped lang="scss">
aside{
    background-color: #F8F8F8;
    width: 90px;
    height: 100vh;
}
.menu__tab{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px 0;
    cursor: pointer;
}
</style>