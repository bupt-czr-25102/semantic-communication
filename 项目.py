"""
语义通信基础演示
作者：曹子蕤
说明：通过简单代码理解语义通信与传统通信的基本区别
项目：北邮智简网络研究室本科生申请演示
"""

def traditional_communication(data):
    """模拟传统通信：传输全部数据"""
    print("传统通信流程：")
    print(f"- 传输原始数据: {len(data)} 字符")
    print(f"- 示例内容: {data[:30]}...")
    return len(data)

def semantic_communication(data):
    """模拟语义通信：传输关键信息"""
    print("语义通信流程：")
    # 简单提取关键词模拟语义理解
    # 此处为手动提取，避免使用完整句子
    keywords = ["语义通信", "信息含义", "传输效率", "新型", "通信方式"]
    print(f"- 提取关键信息: {keywords}")
    # 计算语义数据大小，只计算关键词长度
    semantic_size = sum(len(word) for word in keywords)
    print(f"- 传输语义数据: {semantic_size} 字符")
    return semantic_size

def main():
    """主函数：对比两种通信方式"""
    print("语义通信基础演示")
    print("=" * 50)
    
    # 示例数据
    sample = "语义通信是一种新型通信方式，关注信息的含义而非原始比特，能提高传输效率。"
    
    # 对比两种方式
    traditional_size = traditional_communication(sample)
    semantic_size = semantic_communication(sample)
    
    print("=" * 50)
    print("对比结果：")
    print(f"传统通信数据量: {traditional_size} 字符")
    print(f"语义通信数据量: {semantic_size} 字符")
    
    # 计算并显示传输效率提升
    if traditional_size > 0:
        efficiency_improvement = ((traditional_size - semantic_size) / traditional_size * 100)
        print(f"传输效率提升: {efficiency_improvement:.1f}%")
    
    print("=" * 50)
    print("应用优势：")
    print("1. 多媒体传输：在图片、视频等大数据量传输中，语义通信通过提取关键信息，显著减少传输数据量")
    print("2. 智能交通：支持车联网低延迟、高可靠的通信需求")
    print("3. 智慧城市：优化物联网设备间的通信效率")
    print("4. 远程医疗：确保医疗数据传输的高效性和安全性")
    
    print("=" * 50)
    print("学习心得：")
    print("1. 语义通信通过理解信息含义提高效率")
    print("2. 架构设计比单独算法更重要")
    print("3. 实践是学习通信技术的有效方式")

# 程序入口
if __name__ == "__main__":
    print("北京邮电大学 - 智简网络研究室申请演示")
    print(f"作者: 曹子蕤 | 状态: 自学Python中")
    print()
    main()
    print()
    print("代码说明：")
    print("- 简洁实现，展示核心概念")
    print("- 基于实践学习的理解")
    print("- 关注架构差异而非复杂算法")