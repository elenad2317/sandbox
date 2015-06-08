/**
 * Created by epaz on 6/3/15.
 */

import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._

object sbtTest {
  def main(args: Array[String]): Unit ={
    //println("Well, at least it compiled")
    val logfile = "train.csv"
    val conf = new SparkConf().setAppName("Location Parsing")
    val sc = new SparkContext(conf)
    val csv = sc.textFile(logfile)
    val splitCsv = csv.map(_.split("\t"))
    val subsplit = splitCsv.map{
      b => b(0).split(",")
    }
    val endmap = subsplit.map{
      x => if (x.apply(0).toInt == 1) {0}
           else {x.apply(1).toInt}
    }
    val reduced = endmap.reduce((x, y) => x + y)
    println(reduced)
  }
}
